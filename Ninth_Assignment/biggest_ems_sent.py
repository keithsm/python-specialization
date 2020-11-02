#Assignment 9.4

#Write a program to read through the mbox-short.txt and figure out who
#has sent the greatest number of mail messages. The program looks for
#'From ' lines and takes the second word of those lines as the person
#who sent the mail. The program creates a Python dictionary that maps
#the sender's mail address to a count of the number of times they appear
#in the file. After the dictionary is produced, the program reads through
#the dictionary using a maximum loop to find the most prolific committer.

#Open the file
file = open('mbox-short.txt')

#Define a dictionary
address_list = dict()

#Interate through lines, strip, split, indentify 'From ', save k/v pair to dictionary
for line in file :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        email = words[1]
        address_list[email] = address_list.get(email, 0) + 1

#Iterate through dictionary count values to get highest value.
bigname = None
bigcount = None
for email, count in address_list.items() :
    if bigcount is None or count > bigcount :
        bigname = email
        bigcount = count

#Display key pair
print(bigname, bigcount)
