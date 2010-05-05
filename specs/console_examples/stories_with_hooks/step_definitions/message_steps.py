from pycukes import *
from should_dsl import *


@Then('I should have message1 attr')
def check_attr(context):
    hasattr(context, 'message1') |should_be| True

