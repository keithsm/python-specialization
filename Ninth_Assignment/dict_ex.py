#dictionary example using for/if/else
#"get" has better efficiencies, but this illustrates a plausible method
print('Enter a word:')
word = input()
if word is None or len(word) < 1 :
	word = open('mbox-short.txt')
#	word = word.read()


dictionary = dict()
for letter in word :
	letter = letter.rstrip()
	letter = letter.strip()
	if letter not in dictionary :
		dictionary[letter] = 1
	else :
		dictionary[letter] = dictionary[letter] + 1
print(dictionary)
