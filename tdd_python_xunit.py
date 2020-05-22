# TODO: Invoke tearDown even if method fails
# TODO: Run multiple tests
# TODO: Report collected results
"""
DONE:
# TODO: Invoke test method
# TODO: Invoke setUp first
# TODO: Invoke tearDown afterward
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
        return TestResult()
    def setUp(self):
        pass
    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
    def setUp(self):
        self.log = "setUp "
    def testMethod(self):
        self.log = self.log + "testMethod "
    def tearDown(self):
        self.log = self.log + "tearDown "


class TestResult:
    def __init__(self):
        self.runCount = 1
    def summary(self):
        return "%d run, 0 failed" % self.runCount


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
