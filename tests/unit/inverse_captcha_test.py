import unittest

from solutions import inverse_captcha

part_one_test_cases = [{'input': '1122', 'output': 3},
                       {'input': '1111', 'output': 4},
                       {'input': '1234', 'output': 0},
                       {'input': '91212129', 'output': 9}]

part_two_test_cases = [{'input': '1212', 'output': 6},
                       {'input': '1221', 'output': 0},
                       {'input': '123425', 'output': 4},
                       {'input': '123123', 'output': 12},
                       {'input': '12131415', 'output': 4}]


class TestinverseCaptcha(unittest.TestCase):
    def test_inverse_captcha(self):
        for case in part_one_test_cases:
            self.assertEqual(inverse_captcha.solve(case['input'], 1), case['output'])

    def test_part_two_captcha(self):
        for case in part_two_test_cases:
            self.assertEqual(inverse_captcha.solve(case['input'],
                                                   len(case['input']) // 2), case['output'])


if __name__ == '__main__':
    unittest.main()
