from pycukes import *
from should_dsl import *


@Then('I should have $message attr')
def check_attr(context, message):
    getattr(context, message) |should_be.equal_to| 'msg'
