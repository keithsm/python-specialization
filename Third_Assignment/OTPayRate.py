#Gather and define pay criteria and convert to float.
#Define overtime rate
hrs = input("Enter Hours:")
hrate = input("Enter Hourly Rate:")
hrs = float(hrs)
hrate = float(hrate)
otrate = (1.5 * hrate)

#Calculate and display base pay without overtime
if hrs <= 40 :
    regpay = (hrate * hrs)
    print (regpay)

#Calculate and display first 40 hours at base hourly
#rate and add overtime pay
else :
    regpay = (hrate * 40)
    othrs = (hrs - 40)
    otpay = (othrs * otrate)
    print (regpay + otpay)
