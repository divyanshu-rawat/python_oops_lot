
import car_structure_class, parking_lot_structure_class


class Parking_lot():

	''' parking lot operations and functions are defined in this class '''

	def __init__(self):
		self.parking_slots = {}


	def create_parking_lot(self,no_of_slots):

		no_of_slots = int(no_of_slots)

		if(len(self.parking_slots)) > 0:
			print 'Parking lot already created :)'

		if no_of_slots > 0:
			for x in range(1, no_of_slots + 1):
				obj = parking_lot_structure_class.parking_lot(slot_number = x, available = True )
				self.parking_slots[x] = obj

			print "Created a parking lot with %s slots" % no_of_slots
		else:
			print "Invalid slots value provided"
		return

	def get_nearest_available_slot(self):
													   										#lambda functions are passed as parameters to a function which expects a function objects as parameter like map, reduce, filter functions.
		available_slots = filter(lambda x: x.available ,self.parking_slots.values())        #filter function also returns a list of element,here self.parking_slots.values() returns list of dictionaries
		
		if not available_slots:
			return None

		return sorted(available_slots, key = lambda x: x.slot_number)[0]			#sorted(iterable, key, reverse)

	def park(self, registration_no, color):
		nearest_slot = self.get_nearest_available_slot()
		# print nearest_slot.slot_number

	def leave(self, slot_number):
		print 'leave'

	def status(self):
		print 'status'

	def registration_numbers_for_cars_with_colour(self, colour):
		print 'registration_numbers_for_cars_with_colour'

	def slot_numbers_for_cars_with_colour(self, colour):
		print 'slot_numbers_for_cars_with_colour'

	def slot_number_for_registration_number(self, reg_no):
		print 'slot_number_for_registration_number'








