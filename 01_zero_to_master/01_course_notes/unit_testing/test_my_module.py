import unittest
import my_module


class TestModule(unittest.TestCase):

    def setUp(self):
        print('\n ** Setup method... **')

    def test_do_stuff(self):
        """*** Testing an integer OK ****"""
        param = 5
        expected = 25
        result = my_module.do_stuff(param)
        self.assertEqual(expected, result)

    def test_do_stuff2(self):
        """**** Passing in a string, we get am error ****"""
        param = 'dsffd'
        result = my_module.do_stuff(param)
        self.assertTrue(isinstance(result, ValueError))

    def tearDown(self):
        print('\n ** Clear / Clean method... **')


if __name__ == 'main':
    unittest.main()
# run the tests with this command
# py -m unittest -v
