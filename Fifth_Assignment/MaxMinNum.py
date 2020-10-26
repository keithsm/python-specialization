largest_num = None
smallest_num = None
while True:
  num = input ('Enter a number: ')
  if num == 'done' :
    break
  try :
      num=float(num)
  except :
      print('Invalid input')
      continue
#Determine largest and smallest numbers
  if largest_num is None :
    largest_num = num
  elif num > largest_num :
    largest_num = num
  elif smallest_num == None :
    smallest_num = num
  elif num < smallest_num :
    smallest_num = num
print ('Maximum is', largest_num)
print ('Minimum is', smallest_num)
