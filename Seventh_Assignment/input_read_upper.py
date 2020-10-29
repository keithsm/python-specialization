#Assignment 7.1
#Program that prompts for a file name, then opens that file and
#reads through the file, and print the contents of the file in upper case.

#Input and open the the file
fname = input ('Enter the name of the file: ')
file_contents = open (fname)

#Read the file contents
text = file_contents.read()

#Convert to uppercase and display
uc_text = text.upper()
print (uc_text)
