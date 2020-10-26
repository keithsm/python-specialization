#Declare that we don't have any existing values for
#the largest and smallest numbers we're seeking.
largest_num = None
smallest_num = None

#Define an infinite loop that will run until 'done'
#is entered.
while True:
  num = input ('Enter a number:')
  if num == 'done' : break
  try :
      num=int(num)
  except :
      print('Invalid input')
      continue

#After the first entry, largest_num and smallest_num
#are equal
  largest_num = num
  smallest_num = num

  if largest_num < num :
        largest_num = num
  elif smallest_num > num :
        smallest_num = num

#Determine the largest and smallest numbers
#  if largest_num is None :
#    largest_num = num
#  elif num > largest_num :
#    largest_num = num
# elif smallest_num == None :
#    smallest_num = num
#  elif num < smallest_num :
#    smallest_num = num
print ('Maximum is', largest_num)
print ('Minimum is', smallest_num)
