# TODO: Invoke tearDown afterward
# TODO: Invoke tearDown even if method fails
# TODO: Run multiple tests
# TODO: Report collected results
"""
DONE:
# TODO: Invoke test method
# TODO: Invoke setUp first
# TODO: Log string in WasRun
"""

class TestCase():
    def __init__(self, name):
        self.name = name
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
    def setUp(self):
        pass
    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
    def testMethod(self):
        self.log = self.log + "testMethod "
    def setUp(self):
        self.log = "setUp "
    def tearDown(self):
        self.log = self.log + "tearDown "


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)


TestCaseTest("testTemplateMethod").run()
