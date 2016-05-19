import cleaner as c
import unittest
import sys
import io


class CommandLineTests(unittest.TestCase):
    def setUp(self):
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def testParser(self):
        parser = c.parse_args(['someDirectory'])
        self.assertEqual(parser.resultRoot, 'someDirectory')

    def testTooManyArgs(self):
        self.assertRaises(SystemExit, c.parse_args, ['hej', 'hopp'])
        # also too few arguments
        self.assertRaises(SystemExit, c.parse_args, [])


if __name__ == '__main__':
    unittest.main()
