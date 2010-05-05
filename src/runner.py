from pyhistorian import Story, Scenario
from pyhistorian.language import TEMPLATE_PATTERN
from story_parser import parse_text
import re


class StoryRunner(object):
    def __init__(self, story_text, output, colored,
                 modules=(), language='en-us',
                 before_all=(), before_each=(),
                 after_all=(), after_each=()):
        self._story_text = story_text
        self._output = output
        self._modules = modules
        self._colored = colored
        self._language = language
        self._parsed_story = parse_text(story_text, self._language)
        self._pycukes_story = self._get_pycukes_story()
        self._all_givens = {}
        self._all_whens = {}
        self._all_thens = {}
        self._collect_steps()
        self._before_all = before_all
        self._before_each = before_each
        self._after_all = after_all
        self._after_each = after_each

    def _collect_steps(self):
        for module in self._modules:
            for step_name in ['given', 'when', 'then']:
                steps = getattr(module, '_%ss' % step_name, [])
                for method, message, args in steps:
                    all_this_step = getattr(self, '_all_%ss' % step_name)
                    all_this_step[message] = (method, args)

    def _get_header(self):
        story = self._parsed_story.get_stories()[0]
        return story.header

    def _call_before_each_methods(self, namespace):
        for before_meth in self._before_each:
            before_meth(namespace)

    def _call_before_all_methods(self, namespace):
        for before_meth in self._before_all:
            before_meth(namespace)

    def _call_after_all_methods(self, namespace):
        for after_meth in self._after_all:
            after_meth(namespace)

    def _call_after_each_methods(self, namespace):
        for after_meth in self._after_each:
            after_meth(namespace)

    def _get_pycukes_story(self):
        return type('PyCukesStory',
                    (Story,),
                    {'__doc__' :'\n'.join(self._get_header().split('\n')[1:]),
                     'output': self._output,
                     'title': self._parsed_story.get_stories()[0].title,
                     'colored': self._colored,
                     'scenarios': [],
                     'template_color':'yellow',
                     'language': self._language,
                     'before_each': self._call_before_each_methods,
                     'before_all': self._call_before_all_methods,
                     'after_all': self._call_after_all_methods,
                     'after_each': self._call_after_each_methods,})

    def run(self):
        scenarios = self._parsed_story.get_stories()[0].scenarios
        for scenario_title, steps in scenarios:
            new_scenario = type('PyCukesScenario',
                                (Scenario,),
                                {'__doc__': scenario_title,
                                '_givens': [],
                                '_whens': [],
                                '_thens': [],
                                })

            for step_name in ['given', 'when', 'then']:
                for step_message in steps[step_name]:
                    scenario_steps = getattr(new_scenario, '_%ss' % step_name)
                    all_runner_steps = getattr(self, '_all_%ss' % step_name)
                    actual_scenario = (None, step_message, ())
                    for step_regex, (step_method, step_args) in all_runner_steps.items():
                        msg_pattern = re.sub(TEMPLATE_PATTERN, r'(.*)', step_regex)
                        msg_pattern = re.escape(msg_pattern)
                        msg_pattern = msg_pattern.replace(re.escape(r'(.*)'), r'(.*)')

                        if re.match(msg_pattern, step_message):
                            actual_scenario = (step_method,
                                               step_message,
                                               re.match(msg_pattern,
                                                        step_message).groups())
                    scenario_steps.append(actual_scenario)
 
            self._pycukes_story.scenarios.append(new_scenario)
        return self._pycukes_story.run()
