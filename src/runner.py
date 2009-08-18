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
#        import pdb;pdb.set_trace()
        scenarios = self._parsed_story.get_scenarios()
        for scenario_title, steps in scenarios:
            new_scenario = type('NewScenario',
                                (Scenario,),
                                {'__doc__': scenario_title,
                                '_givens': [],
                                '_whens': [],
                                '_thens': [],
                                })
            for given_message in steps['given']:
                if given_message not in self._all_givens:
                    new_scenario._givens.append( (None, given_message, ()) )
                for given_regex, value in self._all_givens.items():
                    if given_message == given_regex:
                        new_scenario._givens.append( (value[0], given_message, value[1]) )
            
            for when_message in steps['when']:
                if when_message not in self._all_whens:
                    new_scenario._whens.append( (None, when_message, ()) )
                for when_regex, value in self._all_whens.items():
                    if when_regex == when_message:
                        new_scenario._whens.append( (value[0], when_message, value[1]) )

            for then_message in steps['then']:
                if then_message not in self._all_thens:
                    new_scenario._thens.append( (None, then_message, ()) )
                for then_regex, value in self._all_thens.items():
                    if then_regex == then_message:
                        new_scenario._thens.append( (value[0], then_message, value[1]) )

 
            self._pycukes_story.scenarios.append(new_scenario)
        self._pycukes_story.run()
