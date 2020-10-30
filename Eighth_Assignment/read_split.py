#Assignment 8.1
#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words
#using the split() method. The program should build
#a list of words. For each word on each line check
#to see if the word is already in the list and if
#not append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.

text = open('romeo.txt')
input = text.read()
#norm_text = input.lower()
words = input.split()
word_list = list()
for item in words :
    if item not in word_list :
        word_list.append(item)

word_list.sort()
print(word_list)
