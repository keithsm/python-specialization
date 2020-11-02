#Dictionary example using 'get'
#Prints the number of times a given word occurs in a string of text.
print('Enter a string of words:')
string = input()

print('Would you like to know the incidence of letters or words? (l or w) ')
choice = input()

if choice == 'l' :
    stringltrs = string
    dictltrs = dict()
    for stringltrs in string :
        dictltrs[stringltrs] = dictltrs.get(stringltrs,0) + 1
    print(dictltrs)
if choice == 'w' :
    stringwords = string.split()
    dictsplit = dict()
    for words in stringwords :
        dictsplit[words] = dictsplit.get(words,0) + 1
    print(dictsplit)
quit()
