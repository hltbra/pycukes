from pycukes import BeforeAll, AfterAll, BeforeEach, AfterEach


@BeforeAll
def add_message1_attr(context):
    context.counter = 1


@BeforeEach
def add_message_attr(context):
    context.counter += 1
    setattr(context, 'message%d' % context.counter, 'msg')

@AfterEach
def increment_one(context):
    context.counter += 1

@AfterAll
def show_hello_world(context):
    print 'hello world'
