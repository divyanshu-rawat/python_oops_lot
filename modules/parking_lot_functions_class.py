
import car_structure_class, parking_lot_structure_class


class Parking_lot():

	''' parking lot operations and functions are defined in this class '''

	def __init__(self):
		self.parking_slots = {}

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)


	def create_parking_lot(self,no_of_slots):

		no_of_slots = int(no_of_slots)

		if(len(self.parking_slots)) > 0:
			print 'Parking lot already created :)'
			return

		if no_of_slots > 0:
			for x in range(1, no_of_slots + 1):
				obj = parking_lot_structure_class.parking_lot(slot_number = x, available = True )
				self.parking_slots[x] = obj

			print "Created a parking lot with %s slots" % no_of_slots
		else:
			print "Invalid slots value provided"
		return

	def get_nearest_available_slot(self):
		 
		"""key argument in sorted function is used to sort the object by a key, here key implies keys present in the object, in available_slots we have slot_no and available as a key.
        here second argument to the sorted() fn is lambda fn that is iterating over the available_slots slot_no and sorting the available_slots by key. 
        sorted() returning the nearest_slot by sorting an array and returning the value at index 0."""

													   										#lambda functions are passed as parameters to a function which expects a function objects as parameter like map, reduce, filter functions.
		available_slots = filter(lambda x: x.available ,self.parking_slots.values())        #filter function also returns a list of element,here self.parking_slots.values() returns list of dictionaries
		print len(available_slots)
		if not available_slots:
			return None

		return sorted(available_slots, key = lambda x: x.slot_number)[0]			#sorted(iterable, key, reverse)

	def park(self, registration_no, color):
		
		""" Method to park car in nearest parking slot. """

		nearest_slot = self.get_nearest_available_slot()

		if nearest_slot:
			#@classmethod in car class is returning an object.
			nearest_slot.car  = car_structure_class.Car.create_car_object(registration_no,color)
			nearest_slot.available = False
			print 'Car parked at %s slot' % (nearest_slot.slot_number)
		else:
			print "Sorry, parking lot is full."

		# After Parking
		# Car Obj structure should be like this {'_reg_no': 'KA-01-HH-2701', '_colour': 'Blue'}
		# lot structure should be like this {'_available': False, '_slot_no': 1, '_car': <car.Car object at 0x10cad6d10>}


	def leave(self, slot_number):
		print 'leave'
		lot_object = self.parking_slots[int(slot_number)]
		# print lot_object.car.color

		if not lot_object.available and lot_object.car:
			lot_object.available = True
			lot_object.car = None


	def status(self):

		# shows current status of parking

		if self.status_check():
			return

		print "Slot No\tRegistration No\tColour"
		
		for x in self.parking_slots.values(): 					# returns structure similar to this {'_available': False, '_slot_no': 1, '_car': {'_reg_no': 'KA-01-HH-2701', '_colour': 'Blue'}}
			if not x.available and x.car:
				print "%s\t%s\t%s" % (x.slot_no, x.car.reg_no, x.car.colour)

	def registration_numbers_for_cars_with_colour(self, color):

		# print color
		reg_nos = ''

		for lot in self.parking_slots.values():
			if not lot.available and lot.car:
				if lot.car.color == color:
					print lot.car.color



	

	def slot_numbers_for_cars_with_colour(self, color):
		
		for x in self.parking_slots.values():
			if not x.available and x.car:
				if x.car.color == color:
					print x.slot_number

	def slot_number_for_registration_number(self, reg_no):
		print 'slot_number_for_registration_number'



	def status_check(self):
		if(len(self.parking_slots) == 0):
			print 'parking lot not created'
			return True
		return False









