from unittest import TestCase

from exceptions.command_not_found_exception import CommandNotFoundException
from exceptions.invalid_input_exception import InvalidInputException
from services.parser import RequestParser


class TestRequestParser(TestCase):
    def test_parse_valid_command(self):
        parser = RequestParser()
        parser.parse(['Create_parking_lot', '4'])

    def test_parse_valid_command_invalid_num_args(self):
        parser = RequestParser()

        self.assertRaises(InvalidInputException, parser.parse, ['Create_parking_lot'])

    def test_parse_invalid_command(self):
        parser = RequestParser()

        self.assertRaises(CommandNotFoundException, parser.parse, ['Create', '4'])
