#Gather and define pay criteria
hrs = input("Enter Hours:")
hrate = input("Enter Hourly Rate:")
hrs = float(hrs)
hrate = float(hrate)
otrate = (1.5 * hrate)

#Calculate and display base pay without overtime
if hrs <= 40 :
    regpay = (hrate * hrs)
    print (stpay)

#Calculate and display first 40 hours at base hourly
#rate and add overtime pay
elif hrs > 40 :
    regpay = (hrate * 40)
    othrs = (hrs - 40)
    otpay = (othrs * otrate)
    print (regpay + otpay)
