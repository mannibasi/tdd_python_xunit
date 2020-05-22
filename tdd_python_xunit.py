# TODO: Log string in WasRun
# TODO: Invoke tearDown afterward
# TODO: Invoke tearDown even if method fails
# TODO: Run multiple tests
# TODO: Report collected results
"""
DONE:
# TODO: Invoke test method
# TODO: Invoke setUp first
"""

class TestCase():
    def __init__(self, name):
        self.name = name
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
    def setUp(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "
    def setUp(self):
        self.wasRun = None
        self.log = "setUp "


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod " == test.log)


TestCaseTest("testTemplateMethod").run()
