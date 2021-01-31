from unittest import TestCase

from model.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.v = Vehicle('KA 05 FB 1234', 23)

    def test_get_reg_num(self):
        self.assertEqual(self.v.get_reg_num(), 'KA 05 FB 1234')

    def test_get_age(self):
        self.assertEqual(self.v.get_age(), 23)
