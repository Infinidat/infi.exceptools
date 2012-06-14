import nose

from . import exceptools_decorator

class NosePlugin(nose.plugins.Plugin):
    """print chained exceptions"""
    name = 'infi-exceptools'

    def help(self):
        return "Print chained exceptions"

    def prepareTestResult(self, result):
        result.addError = exceptools_decorator(result.addError)
        result.addFailure = exceptools_decorator(result.addFailure)
        return result
