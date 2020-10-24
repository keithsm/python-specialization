#Gather pay criteria
hrs = input("Enter Hours:")
hrate = input("Enter Hourly Rate:")

#Convert 'hrs' and 'hrate' to floating point
hrs = float(hrs)
hrate = float(hrate)

#Define overtime rate
otrate = (1.5 * hrate)

#Calculate and display base pay without overtime
if hrs <= 40 :
    stpay = (hrate * hrs)
    print (stpay)
elif hrs > 40 :
    stpay = (hrate * 40)
    othrs = (hrs - 40)
    otpay = (othrs * otrate)
    print (stpay + otpay)
