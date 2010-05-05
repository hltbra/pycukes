from pycukes import BeforeAll


@BeforeAll
def add_message1_attr(context):
    context.message1 = 'msg'
