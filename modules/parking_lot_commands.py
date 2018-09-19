
import sys
import parking_lot_functions_class


class Parking_commands():

	def __init__(self):
		self.parking_lot_functions_class = parking_lot_functions_class.Parking_lot()

	def input_file_processing(self,entered_file):
		read_file_obj = open(entered_file)  					#Open a file, return an object of the file.
		try:
			while True:
				current_line = read_file_obj.next()				#This method returns the next input line, or raises StopIteration when EOF is hit.
				if current_line.endswith('\n'):
					current_line = current_line[:-1]			#It slices the string to omit the last character, in this case a newline character.
				if current_line == '':
					continue
				self.process_entered_commands(current_line)
		except IOError:
			print 'File not found'
		except StopIteration:
			read_file_obj.close()
		except Exception as error:
			print "Error occured while processing file %s" % error.message

	def user_input(self):
		try:
			while True:
				standard_input = raw_input("Enter Command:")
				self.process_entered_commands(standard_input)
		except(KeyboardInterrupt, SystemExit): 									#Raised when the user hits the interrupt key (normally Control-C or Delete)
			return
		except Exception as error:
			print "Error occured while processing file %s" % error.message


	def process_entered_commands(self,standard_input):
		user_inputs = standard_input.split()                    				#Returns list of commands
		command = user_inputs[0]			   									#['park', '1-2-3', 'blue'] 
		arguments = user_inputs[1:]
		print command,arguments
		if hasattr(self.parking_lot_functions_class, command):
			get_function = getattr(self.parking_lot_functions_class, command) 	#returns the function defined parking_lot_functions_class class, whose name is same as command entered by user .
			get_function(*arguments)											# as we do not know before hand that how many arguments can be passed to our function, for instance creating a lot requires 1 argument, where as park requires 2.
		else:						
			print 'Wrong Command Entered, Please try again!'

# defining this file as the entry point to our program,
# So, The global variable, __name__, in this file,  that is the entry point to your program, is '__main__'


if __name__ == "__main__":
	# sys.argv returns a list of strings representing the arguments (as separated by spaces) on the command-line.
	arguments = sys.argv
	# print(arguments, len(arguments))  # (['./parking_lot_commands.py', 'sample_inputs'], 2)

	if(len(arguments) == 1):
		Parking_commands().user_input()			#process the input
	
	elif (len(arguments) == 2):
		Parking_commands().input_file_processing(arguments[1])    #process the file
	else:
		print "Wrong Number of Arguments Entered"

