# This opens a handle to your file, in 'r' read mode
file_handle = open('day1_input.txt', 'r')
# Read in all the lines of your file into a list of lines
lines_list = file_handle.readlines()
# Extract dimensions from first line. Cast values to integers from strings.
cols, rows = (int(val) for val in lines_list[0].split())
# Do a double-nested list comprehension to get the rest of the data into your matrix
my_data = [[int(val) for val in line.split()] for line in lines_list[1:]]
print(my_data)



