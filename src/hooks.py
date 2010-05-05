from pyhistorian import Step

class BeforeAll(Step):
    name = 'before_all'

class AfterAll(Step):
    name = 'after_all'

class BeforeEach(Step):
    name = 'before_each'

class AfterEach(Step):
    name = 'after_each'
