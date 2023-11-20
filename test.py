import unittest
from io import StringIO
from unittest.mock import patch
from lib import findCommon  # Используйте имя вашего файла, например, lib.py

class TestFindCommon(unittest.TestCase):
    def test_findCommon(self):
        test_cases = [
            {
                'input': ['1 2 3', '2 3 4', '3 4 5'],
                'expected_output': {'2', '3'},
            },
            # Добавьте другие тестовые случаи по необходимости
        ]

        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                findCommon.main()
                actual_output = set(mock_stdout.getvalue().strip().split())
                self.assertEqual(actual_output, test_case['expected_output'])

if __name__ == '__main__':
    unittest.main()