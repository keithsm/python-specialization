#Enter and validate range of input (0.0 - 1.0).
score = input("Enter Score (0.0 - 1.0): ")
score = float(score)
if score < 0.0 :
    print ("Score cannot be less than 0.0. Please retry.")
elif score > 1.0 :
    print ("Score cannot be greater than 1.0). Please retry.")

#Calculate and display grade
elif score >= .9 : print ('A')
elif score >= .8 : print ('B')
elif score >= .7 : print ('C')
elif score >= .6 : print ('D')
elif score < 0.6 : print ('F')
