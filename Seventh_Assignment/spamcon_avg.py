#Assignment 7.2
#A program that prompts for a file name, then opens that
#file and reads through the file, looking for lines of the
#form:
#        X-DSPAM-Confidence:    0.8475
#Counts these lines and extract the floating point values
#from each of the lines and compute the average of those
#values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in
#your solution.

#Input and open the the file
fname = input ('Enter the name of the file: ')
file_contents = open (fname)

#Counts the instances of lines containing:
#'X-DSPAM-Confidence:' and extract floating point
#values from each of the lines and compute the average.
count = 0
spamvaltot = 0
for line in file_contents :
    if line.startswith('X-DSPAM-Confidence:') :
        count = count + 1
        spamconfid = (line[20:])
        spamval = float(spamconfid)
        spamvaltot = spamvaltot + spamval
spamconfavg = spamvaltot/count

#Display
print ('Average spam confidence:',spamconfavg)
