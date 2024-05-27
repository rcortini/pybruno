import unittest
import pathlib
from pybruno.bru_parser import parse_bru_file, parse_env_file

# a global variable representing the absolute path to the current file
current_path = pathlib.Path(__file__).parent.resolve()

class TestBruParser(unittest.TestCase):
    def test_parse_bru_file(self):
        result = parse_bru_file(f'{current_path}/test.bru')
        expected_result = {'meta': {'name': 'Get topics', 'type': 'http', 'seq': '1'}, 'http': {'method': 'get', 'url': '{{baseURL}}/topics', 'body': 'none', 'auth': 'none'}}
        self.assertEqual(result, expected_result)

class TestEnvParser(unittest.TestCase):
    def test_parse_env_file(self):
        result = parse_env_file(f'{current_path}/test_env.bru')
        expected_result = {'baseURL': 'https://api.openalex.org'}
        self.assertEqual(result, expected_result)

class TestBruWithEnvParser(unittest.TestCase):
    def test_parse_bru_with_env_file(self):
        env = parse_env_file(f'{current_path}/test_env.bru')
        result = parse_bru_file(f'{current_path}/test.bru', env)
        expected_result = {'meta': {'name': 'Get topics', 'type': 'http', 'seq': '1'}, 'http': {'method': 'get', 'url': 'https://api.openalex.org/topics', 'body': 'none', 'auth': 'none'}}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()