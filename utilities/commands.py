from enum import Enum


class Commands(Enum):
    """Commands Enum to denote the types of commands available to the user
    """
    CREATE_PARKING_LOT = 'CREATE_PARKING_LOT'
    PARK = 'PARK'
    LEAVE = 'LEAVE'
    SLOT_NUMBERS_FOR_DRIVER_OF_AGE = 'SLOT_NUMBERS_FOR_DRIVER_OF_AGE'
    SLOT_NUMBER_FOR_CAR_WITH_NUMBER = 'SLOT_NUMBER_FOR_CAR_WITH_NUMBER'
    VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE = 'VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE'

    def __str__(self):
        return self.value


class CommandUtils:
    """Utilities class for obtaining more information about the Commands enum items
    """

    COMMAND_LIST = [
        'CREATE_PARKING_LOT',
        'PARK',
        'LEAVE',
        'SLOT_NUMBERS_FOR_DRIVER_OF_AGE',
        'SLOT_NUMBER_FOR_CAR_WITH_NUMBER',
        'VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE'
    ]

    VALIDATION_MAP = {
        Commands.CREATE_PARKING_LOT: 2,
        Commands.PARK: 4,
        Commands.SLOT_NUMBERS_FOR_DRIVER_OF_AGE: 2,
        Commands.SLOT_NUMBER_FOR_CAR_WITH_NUMBER: 2,
        Commands.LEAVE: 2,
        Commands.VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE: 2
    }
