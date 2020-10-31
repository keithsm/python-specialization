#Assignment 8.5

#The logic here is based on the demonstration exercise by Dr. Chuck.
#Still uses a for loop, like I did, but splits the file in the loop,
#error checks each line for validity and grabs the second item [1],
#the email address.  I added the logic for the list and len count,
#though I wonder if there is a way to get the number of addresses
#without using a list.

#Open the file mbox-short.txt and read it line by line.
#When you find a line that starts with 'From ' like the
#following line:
#   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out
#the second word in the line (i.e. the entire address
#of the person who sent the message). Then print out a
#count at the end.

#Hint: make sure not to include the lines that  start
#with 'From:'.

#Open and 'mbox-short' file
file = open('mbox-short.txt')
#Define a list
address_list = list()

#Strip white space, split each line, validate the line contains advantage
#print each address and add each to a list.
for line in file :
    line = line.rstrip()
    words = line.split()
    #Some lines don't have any text, so if no words, continue.
    #Many lines don't start with 'From '.  If True, skip them.
    if len(words) < 1 or words[0] != 'From' :
        continue
    print(words[1])
    address_list.append(words)

#Display
print('There were',(len(address_list)),'lines in the file with From as the first word')
