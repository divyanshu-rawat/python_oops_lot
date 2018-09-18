
import sys
import parking_lot_functions_class


class Parking_commands():

	def __init__(self):
		self.parking_lot_functions_class = parking_lot_functions_class.Parking_lot()

	def input_file_processing(self,entered_file):
		print 'I am in input_file_processing'

	def entered_input(self):
		print 'I am in entered_input'

	def process_entered_commands(self):
		print 'I am in process_entered_commands'

# defining this file as the entry point to our program,
# So, The global variable, __name__, in this file,  that is the entry point to your program, is '__main__'


if __name__ == "__main__":
	# sys.argv returns a list of strings representing the arguments (as separated by spaces) on the command-line.
	arguments = sys.argv
	# print(arguments, len(arguments))  # (['./parking_lot_commands.py', 'sample_inputs'], 2)

	if(len(arguments) == 1):
		Parking_commands().entered_input()			#process the input
	
	elif (len(arguments) == 2):
		Parking_commands().input_file_processing(arguments[1])    #process the file
	else:
		print "Wrong Number of Arguments Entered"

