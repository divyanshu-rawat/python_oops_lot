
import sys



# defining this file as the entry point to our program,
# So, The global variable, __name__, in this file,  that is the entry point to your program, is '__main__'


if __name__ == "__main__":
	# sys.argv returns a list of strings representing the arguments (as separated by spaces) on the command-line.
	arguments = sys.argv
	# print(arguments, len(arguments))  # (['./parking_lot_commands.py', 'sample_inputs'], 2)

	if(len(arguments) == 1):
		#process the input

	elif (len(arguments) == 2):
		#process the file
	else:
		print "Wrong Number of Arguments Entered"

