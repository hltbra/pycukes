from pycukes import BeforeAll, AfterAll, BeforeEach


@BeforeAll
def add_message1_attr(context):
    context.counter = 1


@BeforeEach
def add_message_attr(context):
    setattr(context, 'message%d' % context.counter, 'msg')
    context.counter += 1


@AfterAll
def show_hello_world(context):
    print 'hello world'
