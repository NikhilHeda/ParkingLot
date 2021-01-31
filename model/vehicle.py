class Vehicle:
    def __init__(self, reg_num: str, age: int):
        """Vehicle Model class

        Args:
            reg_num (str): Registration number of the vehicle
            age (int): Age of the driver of the vehicle
        """
        self.reg_num = reg_num
        self.age = age

    def get_reg_num(self) -> str:
        """Getter for the registration number of the vehicle

        Returns:
            str: Returns the registration number for the vehicle
        """
        return self.reg_num

    def get_age(self) -> int:
        """Getter for the age of the driver of the vehicle

        Returns:
            int: Return the age of the driver of the vehicle
        """
        return self.age
