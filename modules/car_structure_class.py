

# class depicts structure of car
class Car():

	def __init__(self):
		self._registration_number = None
		self._color               = None

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

    # @property makes color to work as a getter,helps in Creating functions for managing the getting, setting and deleting of an attribute.
	@property          
	def color(self):
		return self._color

	@color.setter                # setter for color.
	def color(self,value):
		return self._color = value

   
	@property					 # getter for registration_number 
	def registration_number(self):
		return self._registration_number

	@registration_number.setter  # setter for registration_number
	def registration_number(self,value):
		return self._registration_number = value




