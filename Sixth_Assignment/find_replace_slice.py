text = "X-DSPAM-Confidence:    0.8475"

#Find position of a common delimiter ':'
pos=text.find(':')

#Get the balance of the string past the ':'
rawvalue = (text[pos + 1 :])

#strip whitespace and convert string to float and print
convalue = float(rawvalue.strip())
print (convalue)
