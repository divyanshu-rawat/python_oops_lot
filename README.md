

Example:​ ​Interactive

To run the program and launch the terminal:

$ cd modules
$ python parking_lot_commands.py


Input:

create_parking_lot 6

Output:

Created a parking lot with 6 slots

Input:

park KA-01-HH-1234 White

Output:

Allocated slot number: 1

Input:

park KA-01-HH-9999 White

Output:

Allocated slot number: 2

Input:

park KA-01-BB-0001 Black

Output:

Allocated slot number: 3

Input:

park KA-01-HH-7777 Red

Output:

Allocated slot number: 4

Input:

park KA-01-HH-2701 Blue

Output:

Allocated slot number: 5

Input:

park KA-01-HH-3141 Black

Output:

Allocated slot number: 6

Input:

leave 4

Output:

Slot number 4 is free

Input:

status

Output:

Slot No. Registration No. Colour.

1 KA-01-HH- 1234 White

2 KA-01-HH- 9999 White

3 KA-01-BB- 0001 Black

5 KA-01-HH- 2701 Blue

6 KA-01-HH- 3141 Black

Input:

park KA-01-P-333 White

Output:

Allocated slot number: 4

Input:

park DL-12-AA-9999 White

Output:

Sorry, parking lot is full

Input:

registration_numbers_for_cars_with_colour White

Output:

KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333

Input:

slot_numbers_for_cars_with_colour White

Output:

1, 2, 4

Input:

slot_number_for_registration_number KA-01-HH-3141

Output:


6

Input:

slot_number_for_registration_number MH-04-AY-1111

Output:

Not found



Example:​ File

To run the program and launch the terminal:

$ python parking_lot_commands.py sample_inputs.txt


