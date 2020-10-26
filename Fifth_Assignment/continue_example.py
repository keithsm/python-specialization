while True:
  line = input('>')
  #if line[0] reads as "If the first character entered is a pound sign"
  if line[0] == '#' :
    continue
  if line == 'done' :
    break
  print(line)
print('Done!')
