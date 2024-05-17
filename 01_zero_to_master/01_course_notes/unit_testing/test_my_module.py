import unittest
import my_module


class TestModule(unittest.TestCase):
    def test_do_stuff(self):
        param = 5
        expected = 25
        result = my_module.do_stuff(param)
        self.assertEqual(expected, result)

    def test_do_stuff2(self):
        param = 'dsffd'
        result = my_module.do_stuff(param)
        self.assertTrue(isinstance(result, ValueError))


unittest.main()
