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


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = 1
    def run(self):
        method = getattr(self, self.name)
        method()


test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)