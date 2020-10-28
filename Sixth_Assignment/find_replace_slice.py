text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(':')
rawvalue = (text[pos + 1 :])
convalue = rawvalue.strip()
convalue = float(convalue)
print (convalue)
