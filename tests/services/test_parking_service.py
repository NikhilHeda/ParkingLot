from unittest import TestCase
from unittest.mock import Mock

from model.parking_lot import ParkingLot
from model.vehicle import Vehicle
from services.parking_service import ParkingService, parking_lot_validity_check


class TestParkingService(TestCase):
    def test_valid_parking_lot(self):
        service = ParkingService()
        service.create_parking_lot(4)

        # Testing a decorator, by mocking the function to be decorated and checking if the mock was called or not
        test_service_function = Mock()
        decorated_function = parking_lot_validity_check(test_service_function)
        decorated_function(service)

        test_service_function.assert_called_once()

    def test_invalid_parking_lot(self):
        service = ParkingService()

        # Testing a decorator, by mocking the function to be decorated and checking if the mock was called or not
        test_service_function = Mock()
        decorated_function = parking_lot_validity_check(test_service_function)
        decorated_function(service)

        test_service_function.assert_not_called()

    def test_create_parking_lot(self):
        service = ParkingService()
        capacity = service.create_parking_lot(5)

        self.assertIsInstance(service.parking_lot, ParkingLot)
        self.assertEqual(capacity, 5)

    def test_get_reg_number_for_age_with_non_empty_result(self):
        service = ParkingService()
        vehicle_1 = Vehicle('mock_reg_num_1', 22)
        vehicle_2 = Vehicle('mock_reg_num_2', 25)
        vehicle_3 = Vehicle('mock_reg_num_3', 22)

        service.create_parking_lot(3)
        service.park(vehicle_1)
        service.park(vehicle_2)
        service.park(vehicle_3)

        expected = ['mock_reg_num_1', 'mock_reg_num_3']
        self.assertEqual(service.get_reg_number_for_age(22), expected)

    def test_get_reg_number_for_age_with_empty_result(self):
        service = ParkingService()
        vehicle_1 = Vehicle('mock_reg_num_1', 22)
        vehicle_2 = Vehicle('mock_reg_num_2', 25)

        service.create_parking_lot(3)
        service.park(vehicle_1)
        service.park(vehicle_2)

        self.assertEqual(service.get_reg_number_for_age(18), [])

    def test_get_slot_number_for_age_with_non_empty_result(self):
        service = ParkingService()
        vehicle_1 = Vehicle('mock_reg_num_1', 22)
        vehicle_2 = Vehicle('mock_reg_num_2', 25)
        vehicle_3 = Vehicle('mock_reg_num_3', 22)

        service.create_parking_lot(3)
        service.park(vehicle_1)
        service.park(vehicle_2)
        service.park(vehicle_3)

        expected = ['1', '3']
        self.assertEqual(service.get_slot_number_for_age(22), expected)

    def test_get_slot_number_for_age_with_empty_result(self):
        service = ParkingService()
        vehicle_1 = Vehicle('mock_reg_num_1', 22)
        vehicle_2 = Vehicle('mock_reg_num_2', 25)

        service.create_parking_lot(3)
        service.park(vehicle_1)
        service.park(vehicle_2)

        self.assertEqual(service.get_slot_number_for_age(18), [])

    def test_get_slot_number_for_reg_number_valid_vehicle(self):
        service = ParkingService()
        vehicle_1 = Vehicle('mock_reg_num_1', 22)
        vehicle_2 = Vehicle('mock_reg_num_2', 25)

        service.create_parking_lot(3)
        service.park(vehicle_1)
        service.park(vehicle_2)

        self.assertEqual(service.get_slot_number_for_reg_number('mock_reg_num_2'), 2)

    def test_get_slot_number_for_reg_number_invalid_vehicle(self):
        service = ParkingService()
        vehicle_1 = Vehicle('mock_reg_num_1', 22)
        vehicle_2 = Vehicle('mock_reg_num_2', 25)

        service.create_parking_lot(3)
        service.park(vehicle_1)
        service.park(vehicle_2)

        self.assertIsNone(service.get_slot_number_for_reg_number('mock_reg_num_3'))
