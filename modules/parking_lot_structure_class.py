

class parking_lot():

	def __init__(self, slot_number = None, available = None):
		self._slot_number = slot_number
		self._car = None
		self._available = available

	# @property makes color to work as a getter,helps in Creating functions for managing the getting, setting and deleting of an attribute.
	# getter, setter helps to ensure the principle of data encapsulation.
	@property
	def slot_number(self):
		return self._slot_number 

	@slot_number.setter 						# setter for slot_number
	def slot_number(self,value):
		self._slot_number = value

	@property           						# getter for available
	def available(self):
		return self._available

	@available.setter   						# setter for available
	def available(self,value):
		self._available = value

	@property									# getter for car
	def car(self):
		return self._car

	@car.setter									# setter for car
	def car(self,value):
		self._car = value







