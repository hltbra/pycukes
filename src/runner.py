from story_parser import parse_story


class StoryRunner(object):
    def __init__(self, story_text, output, with_colors, modules=[]):
        self._story_text = story_text
        self._output = output
        self._modules = modules
        self._parsed_story = parse_story(story_text)
        self._all_givens = {}
        self._all_whens = {}
        self._all_thens = {}
        self._collect_steps()

    def _collect_steps(self):
        for module in self._modules:
            givens = getattr(module, '_givens', None)
            if givens:
                for meth, msg, args in givens:
                    self._all_givens[msg] = (meth, args)
            whens = getattr(module, '_whens', None)
            if whens:
                for meth, msg, args in whens:
                    self._all_whens[msg] = (meth, args)   
            thens = getattr(module, '_thens', None)
            if thens:
                for meth, msg, args in thens:
                    self._all_thens[msg] = (meth, args)   

    def run(self):
        for line in ['Story: '+self._parsed_story.get_story_title(),
                     'As a '+self._parsed_story.get_story_role(),
                     'I want to '+self._parsed_story.get_story_feature(),
                     'So that '+self._parsed_story.get_story_businness_value(),
                     ]:
            self._output.write(line + '\n')
        scenarios = self._parsed_story.get_scenarios()
        index = 1
        for scenario_title, steps in scenarios:
            self._output.write('Scenario %d: %s\n' % (index, scenario_title))
            index += 1
            for step_name in ['given', 'when', 'then']:
                for step_message in steps[step_name]:
                    all_steps = getattr(self, '_all_%ss' % step_name)
                    if all_steps:
                        for step_method, step_args in all_steps.values():
                            try:
                                step_method(1)
                                self._output.write('   %s %s   ... OK\n' % (step_name.capitalize(),
                                                                            step_message))

                            except:
                                self._output.write('   %s %s   ... FAIL\n' % (step_name.capitalize(),
                                                                            step_message))

                             
                    else:
                        self._output.write('   %s %s   ... PENDING\n' % (step_name.capitalize(),
                                                                    step_message))
