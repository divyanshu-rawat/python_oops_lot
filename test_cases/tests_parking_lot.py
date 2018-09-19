
import unittest
import env
from modules import parking_lot_functions_class

 ##A testcase is created by subclassing unittest.TestCase.
class ParkingLotTest(unittest.TestCase):  #A testcase is created by subclassing unittest.TestCase.
    
    @classmethod
    def setUpClass(cls):
        cls.parking = parking_lot_functions_class.Parking_lot()
        cls.allocated_slot = 1

    def test_for_creat_a_lot(self):
        parking_slots = 6
        self.parking.create_parking_lot(parking_slots)
        self.assertEqual(len(self.parking.parking_slots), parking_slots, msg="Wrong parking lot created")





if __name__ == '__main__':
    unittest.main()