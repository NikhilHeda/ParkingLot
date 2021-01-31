from model.vehicle import Vehicle


class ParkingLot:
    """Parking lot model class, contains functionality to work with a parking lot structure

    Attributes:
        capacity (int): Maximum number of slots in the parking lot
        slots (list): List of slots in the parking lot, will contain a Vehicle instance if vehicle is parked at that slot, else will contain None
        filled_slots (int): Current number of vehicles parked in the parking lot
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.filled_slots = 0

    def fill_slot(self, vehicle: Vehicle):
        """Method to add a vehicle to a parking slot

        Args:
            vehicle (Vehicle): Vehicle to add

        Returns:
            [int, None]: If succeeds, returns slot_id (slot number) at which the vehicle was parked, else returns None
        """
        if self.is_empty():
            slot_id = self.get_empty_slot()
            self.slots[slot_id] = vehicle
            self.filled_slots += 1
            return slot_id + 1

        print('Parking lot is full! Sorry!')

    def empty_slot(self, slot_id: int):
        """Method to remove a vehicle from a parking slot

        Args:
            slot_id (int): Slot number to vacate

        Returns:
            [Vehicle, None]: If succeeds, returns the vehicle that was parked at slot_id, else returns None
        """

        # Handle error conditions first:
        # Check if parking lot is empty
        if self.filled_slots == 0:
            print('Parking lot is empty! Business is bad...')
            return None

        # Check if slot_id is valid
        if slot_id < 1 or slot_id > self.capacity:
            print('slot_id does not exist! Are you at the correct parking lot?')
            return None

        # Check if the slot is already vacant
        if self.slots[slot_id - 1] is None:
            print('Slot already vacant!')
            return None

        # Parking lot is not empty, slot_id is valid and also not vacant! -> we are good to return the vehicle!
        vehicle = self.slots[slot_id - 1]
        self.slots[slot_id - 1] = None
        self.filled_slots -= 1
        return vehicle

    def is_empty(self):
        """Helper function to indicate if there are empty slots in the parking lot

        Returns:
            bool: True, if slots are available, False otherwise
        """
        return self.filled_slots < self.capacity

    def get_empty_slot(self):
        """Method the get the nearest available slot to park a new vehicle

        Returns:
            int: slot_id where the new vehicle can be parked
        """
        return self.slots.index(None) if self.is_empty() else None

    def get_capacity(self):
        """Getter method to get the capacity of the parking lot

        Returns:
            int: Returns the capacity of the parking lot
        """
        return self.capacity

    def get_slots(self):
        """Getter method to return the current state of the parking slots

        Returns:
            List[int]: Returns the parking slots
        """
        return self.slots
