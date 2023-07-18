# creating variable to store the
# number of words
N_O_W = 0

# Opening our text file in read only
# mode using the open() function
with open(r'sample.txt','r',encoding="utf-8") as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	     data = file.read()

	# Splitting the data into separate lines
	# using the split() function
lines = data.split()

	# Adding the length of the
	# lines in our number_of_words
	# variable
N_O_W += len(lines)


# Printing total number of words
print(N_O_W)
