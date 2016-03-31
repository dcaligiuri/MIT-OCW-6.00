import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def get_word_score(word, n):
    wordScore = 0
    for x in range(0,len(word)):
        x = word[x]
        letterScore = SCRABBLE_LETTER_VALUES[x]
        wordScore = letterScore + wordScore
    if len(word) == n:
        wordScore = wordScore + 50
    return wordScore




def display_hand(hand):
   
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line



def deal_hand(n):
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand





def updateHand(hand,word):
	dictWord = get_frequency_dict(word)
	dictHand = hand
	for x in range(0,len(word)):
		y = word[x]
		if y in dictHand.keys():
			if dictHand[y] > 1:
				dictHand[y] = dictHand[y] - dictWord[y]
			elif dictHand[y] == 1:
				del dictHand[y]
	return dictHand





def is_valid_word(word, hand, word_list):
    for x in range(0,len(word_list)):
        y = word_list[x]
        if y == word:
            dictHand = hand
            dictWord = get_frequency_dict(word)
            for k in range(0,len(word)):
                z = word[k]
                if z in dictHand.keys():
                    if dictHand[z] < dictWord[z]:
                        break
		    else: return True
		else: return False
    else: return False



def play_hand(hand, word_list):
        totalScore = 0
        while totalScore < 10000:
            print 'Current Hand:',
            display_hand(hand)
            word = raw_input('Enter word, or a . to indicate that you are finished: ')
            n = HAND_SIZE
            if word == '.':
                return 0
            elif hand == {}:
                print 'Fine Score: ' + str(totalScore) + ' points'
            elif is_valid_word(word,hand,word_list) is True:
                print word + ' earned ' + str(get_word_score(word,n)) + ' points. ',
                totalScore = totalScore + get_word_score(word,n)
                print 'Total: ' + str(totalScore) + ' points'
                updateHand(hand,word)
            elif is_valid_word(word,hand,word_list) == False:
                print 'Invalid word, please try again.'


def play_game(word_list):
    hand = deal_hand(HAND_SIZE) 
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

word_list = load_words()
play_game(word_list)
