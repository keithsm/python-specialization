#Assignment 8.4
#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words
#using the split() method. The program should build
#a list of words. For each word on each line check
#to see if the word is already in the list and if
#not append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.

#Open romeo.txt file and read input
#Open romeo.txt file and read input
text = open('romeo.txt')
input = text.read()

#Split the input and define an empty list
words = input.split()
word_list = list()

#For each word determine if it's already in the
#word_list. If not, add it.
for item in words :
    if item not in word_list :
        word_list.append(item)

#Sort and display
word_list.sort()
print(word_list)
