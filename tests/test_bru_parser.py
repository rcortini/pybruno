import unittest
from pybruno.bru_parser import parse_bru_file

class TestBruParser(unittest.TestCase):
    def test_parse_bru_file(self):
        result = parse_bru_file('path/to/test.bru')
        expected_result = {"key": "value"}  # Expected result based on your test BRU file
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()