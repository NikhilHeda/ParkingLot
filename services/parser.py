from exceptions.command_not_found_exception import CommandNotFoundException
from exceptions.invalid_input_exception import InvalidInputException
from model.vehicle import Vehicle
from services.parking_service import ParkingService
from utilities.commands import Commands, CommandUtils


class RequestParser:
    """Parser class for parsing and executing user commands.

    Attributes:
        parking_service (ParkingService): Instance of the parking service, will be used to execute user commands
    """

    def __init__(self):
        self.parking_service = ParkingService()

    def parse(self, params):
        """Method to parse (command to execution process) a single line of commands, broken into tokens

        Args:
            params (List[str]): List of tokens obtained from single user command

        Raises:
            CommandNotFoundException: Raised when the user command is invalid.
            InvalidInputException: Raised when the command is valid, but the number of arguments don't match the required number
        """
        command_str = params[0].upper()
        if command_str not in CommandUtils.COMMAND_LIST:
            raise CommandNotFoundException(command_str)

        command = Commands[command_str]
        if len(params) != CommandUtils.VALIDATION_MAP[command]:
            raise InvalidInputException(command, params)

        self.execute_command(command, params[1:])

    def execute_command(self, command, params):
        """Method to execute a valid command

        Args:
            command (Commands): Command enum, denoting the command to be executed
            params (List[str]): List of string parameters required to execute the command
        """
        if command == Commands.CREATE_PARKING_LOT:
            capacity = self.parking_service.create_parking_lot(capacity=int(params[0]))
            print(f'Created parking of {capacity} slots')
        elif command == Commands.PARK:
            vehicle = Vehicle(reg_num=params[0], age=int(params[2]))
            slot_id = self.parking_service.park(vehicle=vehicle)
            if slot_id:
                print(
                    f'Car with vehicle registration number "{vehicle.get_reg_num()}" has been parked at slot number {slot_id}'
                )
        elif command == Commands.LEAVE:
            vehicle = self.parking_service.leave(slot_id=int(params[0]))
            if vehicle:
                print(
                    f'Slot number {params[0]} vacated, the car with vehicle registration number "{vehicle.get_reg_num()}" left the space, the driver of the car was of age {vehicle.get_age()}'
                )
        elif command == Commands.SLOT_NUMBER_FOR_CAR_WITH_NUMBER:
            slot_id = self.parking_service.get_slot_number_for_reg_number(reg_num=params[0])
            if slot_id:
                print(slot_id)
            else:
                print('Vehicle not found.')
        elif command == Commands.SLOT_NUMBERS_FOR_DRIVER_OF_AGE:
            slot_ids = self.parking_service.get_slot_number_for_age(age=int(params[0]))
            if slot_ids:
                print(','.join(slot_ids))
            else:
                print('null')
        elif command == Commands.VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE:
            reg_nums = self.parking_service.get_reg_number_for_age(age=int(params[0]))
            if reg_nums:
                print(','.join(reg_nums))
            else:
                print('null')
