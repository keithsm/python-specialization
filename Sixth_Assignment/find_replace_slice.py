text = "X-DSPAM-Confidence:    0.8475"
trimtext = text.replace(' ', '')
convalue = (trimtext[19:25])
convalue = float(convalue)
print (convalue)
