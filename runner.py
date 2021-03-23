from tests.test_login import TestLogin
from tests.test_registration import TestRegistration
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    suite.addTests(loader.loadTestsFromTestCase(TestRegistration))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
