# TODO: Invoke test method
# TODO: Invoke setUp first
# TODO: Invoke tearDown afterward
# TODO: Invoke tearDown even if method fails
# TODO: Run multiple tests
# TODO: Report collected results
"""
DONE:

"""

class TestCase():
    def __init__(self, name):
        self.name = name
    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = 1


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
        print("Test completed")

        
TestCaseTest("testRunning").run()