from model.parking_lot import ParkingLot
from model.vehicle import Vehicle


def parking_lot_validity_check(method):
    """Decorator for checking if the parking lot is valid or not

    Args:
        method (callable): Function to be decorated => class methods of ParkingService class
    """

    def wrapper(self, *args, **kwargs):
        """Methods checks if the parking lot is initialized or not
        """
        if self.parking_lot is None:
            print('Parking lot is invalid')
            return None
        return method(self, *args, **kwargs)

    return wrapper


class ParkingService:
    """Service class offering parking services like create lot, park car, leave and other information about parking lot

    Attributes:
        parking_lot (ParkingLot): Instance of the parking lot, instantiated when create_parking_lot() is called
    """

    def __init__(self):
        self.parking_lot = None

    def create_parking_lot(self, capacity: int):
        """Creates a parking lot instance with the given capacity

        Args:
            capacity (int): Maximum number of slots in the parking lot

        Returns:
            int: Returns the capacity of the parking lot created
        """
        self.parking_lot = ParkingLot(capacity)
        return self.parking_lot.get_capacity()

    @parking_lot_validity_check
    def park(self, vehicle: Vehicle):
        """Parks a vehicle at an available slot in the parking lot

        Args:
            vehicle (Vehicle): vehicle to be parked

        Returns:
            [int, None]: If succeeds, returns the slot number where the vehicle was parked, else returns None
        """
        return self.parking_lot.fill_slot(vehicle)

    @parking_lot_validity_check
    def leave(self, slot_id: int):
        """Vacates a slot (given slot_id) from the parking lot if any vehicle is parked

        Args:
            slot_id (int): Slot number to vacate

        Returns:
            [Vehicle, None]: If succeeds, returns the vehicle vacated, else returns None
        """
        return self.parking_lot.empty_slot(slot_id)

    @parking_lot_validity_check
    def get_reg_number_for_age(self, age: int):
        """Method to get registration number of all vehicles parked by driver of given age

        Args:
            age (int): Age of the driver

        Returns:
            List[str]: Returns a list of registration numbers
        """
        result = []
        for vehicle in self.parking_lot.get_slots():
            if vehicle and vehicle.get_age() == age:
                result.append(vehicle.get_reg_num())

        return result

    @parking_lot_validity_check
    def get_slot_number_for_age(self, age: int):
        """Method to get slot numbers of all parked vehicles driven by drivers of the given age

        Args:
            age (int): Age of the driver to query on

        Returns:
            List[int]: Returns a list of slot numbers
        """
        result = []
        for slot_id, vehicle in enumerate(self.parking_lot.get_slots(), start=1):
            if vehicle and vehicle.get_age() == age:
                result.append(str(slot_id))

        return result

    @parking_lot_validity_check
    def get_slot_number_for_reg_number(self, reg_num: str):
        """Method to get the slot number for the vehicle with the given registration number

        Args:
            reg_num (str): Registration number of the vehicle

        Returns:
            [int, None]: If succeeds, returns the slot number of the vehicle, else returns None
        """
        slots = self.parking_lot.get_slots()
        for slot_id, vehicle in enumerate(slots, start=1):
            if vehicle is not None and vehicle.get_reg_num() == reg_num:
                return slot_id

        return None

    @parking_lot_validity_check
    def print_parking_lot(self):
        """Debug method to print the current state of the parking lot
        """
        for slot_id, vehicle in enumerate(self.parking_lot.get_slots(), start=1):
            if vehicle:
                print(f'{slot_id} : {vehicle.get_reg_num()}, {vehicle.get_age()}')
