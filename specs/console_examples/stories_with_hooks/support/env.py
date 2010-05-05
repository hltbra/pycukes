from pycukes import BeforeAll, AfterAll


@BeforeAll
def add_message1_attr(context):
    context.message1 = 'msg'
    context.counter = 1


@AfterAll
def show_hello_world(context):
    print 'hello world'
