from unittest import TestCase

from model.parking_lot import ParkingLot
from model.vehicle import Vehicle


class TestParkingLot(TestCase):
    def test_fill_slot_parking_slot_available(self):
        lot = ParkingLot(1)
        vehicle = Vehicle('mock_reg_num', 22)

        result = lot.fill_slot(vehicle)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_fill_slot_parking_lot_full(self):
        lot = ParkingLot(0)
        vehicle = Vehicle('mock_reg_num', 22)

        result = lot.fill_slot(vehicle)
        self.assertIsNone(result)

    def test_empty_slot_valid_slot_id(self):
        lot = ParkingLot(1)
        vehicle = Vehicle('mock_reg_num', 22)

        slot_id = lot.fill_slot(vehicle)

        result = lot.empty_slot(slot_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, Vehicle)
        self.assertEqual(result.get_reg_num(), 'mock_reg_num')
        self.assertEqual(result.get_age(), 22)

    def test_empty_slot_empty_parking_lot(self):
        lot = ParkingLot(1)
        result = lot.empty_slot(1)

        self.assertIsNone(result)

    def test_empty_slot_valid_slot_id_vacant_slot(self):
        lot = ParkingLot(2)

        vehicle = Vehicle('mock_reg_num', 22)
        lot.fill_slot(vehicle)

        result = lot.empty_slot(2)

        self.assertIsNone(result)

    def test_empty_slot_invalid_slot_id(self):
        lot = ParkingLot(1)
        vehicle = Vehicle('mock_reg_num', 22)

        lot.fill_slot(vehicle)
        result = lot.empty_slot(2)

        self.assertIsNone(result)

    def test_is_empty_true_case(self):
        lot = ParkingLot(1)
        self.assertTrue(lot.is_empty())

    def test_is_empty_false_case(self):
        lot = ParkingLot(1)
        vehicle = Vehicle('mock_reg_num', 22)

        lot.fill_slot(vehicle)

        self.assertFalse(lot.is_empty())

    def test_get_empty_slot_available(self):
        lot = ParkingLot(3)
        vehicle_1 = Vehicle('mock_reg_num_1', 22)
        vehicle_2 = Vehicle('mock_reg_num_2', 25)
        vehicle_3 = Vehicle('mock_reg_num_3', 21)

        self.assertEqual(lot.get_empty_slot(), 0)

        lot.fill_slot(vehicle_1)
        slot_id_2 = lot.fill_slot(vehicle_2)
        lot.fill_slot(vehicle_3)

        lot.empty_slot(slot_id_2)

        self.assertEqual(lot.get_empty_slot(), 1)

    def test_get_empty_slot_unavailable(self):
        lot = ParkingLot(0)
        self.assertIsNone(lot.get_empty_slot())

    def test_get_capacity(self):
        lot = ParkingLot(5)
        self.assertEqual(lot.get_capacity(), 5)

    def test_get_slots(self):
        lot = ParkingLot(3)

        vehicle_1 = Vehicle('mock_reg_num_1', 22)
        lot.fill_slot(vehicle_1)
        self.assertEqual(lot.get_slots(), [vehicle_1, None, None])

        vehicle_2 = Vehicle('mock_reg_num_2', 25)
        slot_id_2 = lot.fill_slot(vehicle_2)
        self.assertEqual(lot.get_slots(), [vehicle_1, vehicle_2, None])

        vehicle_3 = Vehicle('mock_reg_num_3', 21)
        lot.fill_slot(vehicle_3)

        lot.empty_slot(slot_id_2)

        self.assertEqual(lot.get_slots(), [vehicle_1, None, vehicle_3])
