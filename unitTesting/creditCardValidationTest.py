import unittest
from creditCardValidation import *

# Unit Test Method
# If both tests pass, it will return OK


class CreditCardValidationTest(unittest.TestCase):

    # We can setup and teardown data for each test
    def setUp(self):
        print('Setup')

    def test_validateCard_valid(self):
        result = validateCard(date(2024,2,2))
        self.assertEqual('Valid', result)

    # We used Assert for Exception in the expired method
    def test_validateCard_expired(self):
        with self.assertRaises(RuntimeError):
            validateCard(date(2089, 2, 2))

    def tearDown(self):
        print('tearDown')


# In Pycharm we don't need the code below for unit test
if __name__ == '__main__':
    unittest.main()
