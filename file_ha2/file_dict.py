#converting the given file to a dictionary

#an empty dictionary
import io
dictionary = {}
with io.open("lang.txt", encoding="utf-8") as file:

    for line in file:

        (key, value) = line.split()

dictionary[int(key)] = value

print ('\ntext file to dictionary=\n',dictionary)
