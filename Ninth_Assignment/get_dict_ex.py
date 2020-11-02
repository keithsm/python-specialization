#Dictionary example using 'get'
#Prints the number of times a given letter or word occurs in a string of text.
print('Enter a string of words:')
string = input()

print('Would you like to know the incidence of letters or words? (l or w) ')
choice = input()

if choice == 'l' :
    stringltrs = string
    dictltrs = dict()
    for stringltrs in string :
        dictltrs[stringltrs] = dictltrs.get(stringltrs,0) + 1

#Create a list. Iterate through dictionary and add tuples to the list.
#Sort the list and display.
    letters_list = list()
    for stringltrs, lcounts in dictltrs.items() :
        lvalues = (stringltrs, lcounts)
        letters_list.append(lvalues)
        letters_list = sorted(letters_list)
    print(letters_list)

if choice == 'w' :
    stringwords = string.split()
    dictsplit = dict()
    for words in stringwords :
        dictsplit[words] = dictsplit.get(words,0) + 1

    words_list = list()
    for words, wcounts in dictsplit.items() :
        wvalues = (words, wcounts)
        words_list.append(wvalues)
        words_list = sorted(words_list)
    print(words_list)
