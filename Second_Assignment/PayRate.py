#Gather pay criteria
hrs = input("Enter Hours:")
hrate = input("Enter Hourly Rate:")

#Convert 'hrs' and 'hrate' to floating point
hrs = float(hrs)
hrate = float(hrate)

#Calculate Gross Pay
gropay=(hrs*hrate)

#Alternate approach from Dr Chuck.  Reduces to 4 lines of code vs 6.
#gropay=float(hrs) * float(hrate)

#Display Output
print("Pay:",gropay)
