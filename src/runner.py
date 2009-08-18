from pyhistorian import Story, Scenario
from story_parser import parse_story


class StoryRunner(object):
    def __init__(self, story_text, output, colored, modules=[]):
        self._story_text = story_text
        self._output = output
        self._modules = modules
        self._colored = colored
        self._parsed_story = parse_story(story_text)
        self._pycukes_story = self._get_pycukes_story()
        self._all_givens = {}
        self._all_whens = {}
        self._all_thens = {}
        self._collect_steps()

    def _collect_steps(self):
        for module in self._modules:
            for step_name in ['given', 'when', 'then']:
                steps = getattr(module, '_%ss' % step_name)
                if steps:
                    for method, message, args in steps:
                        all_this_step = getattr(self, '_all_%ss' % step_name)
                        all_this_step[message] = (method, args)

    def _get_header(self):
        return '\n'.join(['Story: '+self._parsed_story.get_story_title(),
                     'As a '+self._parsed_story.get_story_role(),
                     'I want to '+self._parsed_story.get_story_feature(),
                     'So that '+self._parsed_story.get_story_businness_value(),
                     ])

    def _get_pycukes_story(self):
        return type('Calculator',
                    (Story,),
                    {'__doc__' :'\n'.join(self._get_header().split('\n')[1:]),
                     'output': self._output,
                     'colored': self._colored,
                     'scenarios': [],})

    def run(self):
        scenarios = self._parsed_story.get_scenarios()
        for scenario_title, steps in scenarios:
            new_scenario = type('NewScenario',
                                (Scenario,),
                                {'__doc__': scenario_title,
                                '_givens': [],
                                '_whens': [],
                                '_thens': [],
                                })
            for given, value in self._all_givens.items():
                new_scenario._givens.append( (value[0], given, value[1]) )
            for when, value in self._all_whens.items():
                new_scenario._whens.append( (value[0], when, value[1]) )
            for then, value in self._all_thens.items():
                new_scenario._thens.append( (value[0], then, value[1]) )

            for given in steps['given']:
                if given not in self._all_givens:
                    new_scenario._givens.append( (None, given, ()) )
            for when in steps['when']:
                if when not in self._all_whens:
                    new_scenario._whens.append( (None, when, ()) )
            for then in steps['then']:
                if then not in self._all_thens:
                    new_scenario._thens.append( (None, then, ()) )
 
            self._pycukes_story.scenarios.append(new_scenario)
        self._pycukes_story.run()
