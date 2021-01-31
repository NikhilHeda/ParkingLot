from unittest import TestCase

from exceptions.invalid_input_exception import InvalidInputException
from utilities.commands import Commands


class TestInvalidInputException(TestCase):
    def test_message(self):
        try:
            raise InvalidInputException(Commands.PARK, ['park', 'mock_reg_num', '22'])
        except InvalidInputException as e:
            expected_message = '''Input is invalid for command "PARK", expected 3 arguments, got 2
	['park', 'mock_reg_num', '22']'''
            self.assertEqual(expected_message, str(e))
