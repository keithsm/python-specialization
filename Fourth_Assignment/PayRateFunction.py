#Assignment 4 - Application to define pay using a function

#Gather and define pay criteria and convert to float.
hrs = input("Enter Hours:")
hrate = input("Enter Hourly Rate:")
hrs = float(hrs)
hrate = float(hrate)

#Function to calculate and display base pay with
#or without overtime.
def computepay (hrs, hrate) :
    if hrs <= 40 :
        pay = (hrate * hrs)
        return pay
    else :
        otregpay = (hrate * 40)
        othrs = (hrs - 40)
        otrate = (1.5 * hrate)
        pay = ((othrs * otrate) + otregpay)
        return pay

#Print regular or OT pay
print ('Pay', computepay (hrs, hrate))
