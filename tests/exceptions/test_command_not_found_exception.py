from unittest import TestCase

from exceptions.command_not_found_exception import CommandNotFoundException


class TestCommandNotFoundException(TestCase):
    def test_message(self):
        try:
            raise CommandNotFoundException('invalid_command')
        except CommandNotFoundException as e:
            expected_message = "invalid_command not found in ['CREATE_PARKING_LOT', 'PARK', 'LEAVE', 'SLOT_NUMBERS_FOR_DRIVER_OF_AGE', 'SLOT_NUMBER_FOR_CAR_WITH_NUMBER', 'VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE']\n"
            self.assertEqual(expected_message, str(e))
