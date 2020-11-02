#Assignment 10.2
#Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull
#the hour out from the 'From ' line by finding the time and then splitting
#the string a second time using a colon.
#      From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown in the "Desired Output".

#Specify or open the 'mbox-short.txt' file
filename = input("Enter filename:")
if len(filename) < 1 : filename = "mbox-short.txt"
contents = open(filename)
email_per_hour = dict()

#Loop to grab the hour from each email matching the criteria
for line in contents :
    line = line.rstrip()
    if line.startswith('From ') :
        time = line.split()[5]
        hr = time.split(':')[0]
        email_per_hour[hr] = email_per_hour.get(hr,0) + 1

#Add the values to a list and sort
sorted_by_hour = list()
for hour, count in email_per_hour.items() :
    values = (hour, count)
    sorted_by_hour.append(values)
    sorted_by_hour = sorted(sorted_by_hour)

#Display
for hour, count in sorted_by_hour :
    print (hour, count)
