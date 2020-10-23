#Gather pay criteria
hrs = input("Enter Hours:")
hrate = input("Enter Hourly Rate:")

#Convert 'hrs' and 'hrate' to floating point
hrs = float(hrs)
hrate = float(hrate)

#Calculate Gross Pay
gropay=(hrs*hrate)

#Display Output
print("Pay:",gropay)
