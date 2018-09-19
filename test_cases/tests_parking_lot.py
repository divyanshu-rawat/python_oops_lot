
import unittest
import env
from modules import parking_lot_functions_class

 ##A testcase is created by subclassing unittest.TestCase.
class ParkingLotTest(unittest.TestCase):  #A testcase is created by subclassing unittest.TestCase.
    
    @classmethod
    def setUpClass(cls):
        cls.parking = parking_lot_functions_class.Parking_lot()
        cls.parked_slot = 1
        cls.registration_number = "KA-01-BB-0001"
        cls.color = "Black"

    def test_a_creating_a_lot(self):
        parking_slots = 6
        self.parking.create_parking_lot(parking_slots)
        self.assertEqual(len(self.parking.parking_slots), parking_slots, msg="Wrong parking lot created")

    def test_b_park(self):
        
        self.parking.park(self.registration_number, self.color)

        self.assertFalse(self.parking.parking_slots[self.parked_slot].available, "Park failed.")

        for x in self.parking.parking_slots.values():
            if not x.available and x.car:
                self.assertEqual(x.car.registration_number, self.registration_number, "Park failed")
                self.assertEqual(x.car.color, self.color, "Park failed")

    def test_c_registration_numbers_for_cars_with_colour(self):
    	for x in self.parking.parking_slots.values():
            if not x.available and x.car:
            	if x.car.color == self.color:
            		self.assertEqual(x.car.registration_number, self.registration_number , "Park failed")

    def test_d_slot_numbers_for_cars_with_colour(self):
    	for x in self.parking.parking_slots.values():
            if not x.available and x.car:
            	if x.car.color == self.color:
            		self.assertEqual(x.slot_number, self.parked_slot , "Park failed")

    def test_e_slot_number_for_registration_number(self):
    	for x in self.parking.parking_slots.values():
            if not x.available and x.car:
            	if x.car.registration_number == self.registration_number:
            		self.assertEqual(x.slot_number, self.parked_slot , "Park failed")

    def test_f_leave(self):
    	self.parking.leave(self.parked_slot)
        self.assertTrue(self.parking.parking_slots[self.parked_slot].available, "Leave failed.")



if __name__ == '__main__':
    unittest.main()