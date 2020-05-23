# TODO: Create TestSuite from a TestCase class
# TODO: Run multiple tests
# TODO: Report collected results
"""
DONE:
# TODO: Invoke test method
# TODO: Invoke setUp first
# TODO: Invoke tearDown afterward
# TODO: Invoke tearDown even if method fails
# TODO: Log string in WasRun
"""

class TestCase():
    def __init__(self, name):
        self.name = name
    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except TestFailureException:
            result.testFailed()
        self.tearDown()
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
    def testBrokenMethod(self):
        raise TestFailureException
    def tearDown(self):
        self.log = self.log + "tearDown "


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def testFailed(self):
        self.errorCount = self.errorCount + 1
    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)


class TestSuite:
    def __init__(self):
        self.tests = []
    def add(self, test):
        self.tests.append(test)
    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestFailureException(Exception):
    pass


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testTemplateMethod(self):
        result = TestResult()
        test = WasRun("testMethod")
        test.run(result)
        assert("setUp testMethod tearDown " == test.log)
    def testResult(self):
        result = TestResult()
        test = WasRun("testMethod")
        test.run(result)
        assert("1 run, 0 failed" == result.summary())
    def testFailedResult(self):
        result = TestResult()
        test = WasRun("testBrokenMethod")
        test.run(result)
        assert("1 run, 1 failed" == result.summary())
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())
    def testSuite(self):
        suite = TestSuite()
        result = TestResult()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())