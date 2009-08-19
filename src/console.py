from finder import find_steps_modules, find_text_specs
from runner import StoryRunner

def pycukes_console(specs_dir, steps_dir, output):
    modules = find_steps_modules(steps_dir)
    for spec in find_text_specs(specs_dir):
        StoryRunner(spec, output, colored=False, modules=modules).run()
