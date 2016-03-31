import random
import string



WORDLIST_FILENAME = "words.txt"

def load_words():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq





def ghost():
    print 'Welcome to Ghost!'
    print 'Player 1 goes first'
    buildWord = '\'\''
    for p in range(1,10):
        if p % 2 == 0:
            askLetter(n,buildWord)
            checkWord(buildWord)
        else:
            ask(1)
            check()





def askLetter(n,buildWord):
    print 'Player' + str(n) + 'goes first.'
    print 'Current word fragment' + buildWord
    buildWord = raw_input('Player' + str(n) + 'says letter: ')

def checkWord(buildWord):
    for words in range(0,len(wordlist)):
        if buildWord == wordlist[words] and len(buildWord) > 3:
            break
        for letter in range(0,len(string.ascii_lowercase)):
            y = string.ascii_lowercase[letter]
            if buildWord + letter == wordlist[words] and len(buildWord) > 3):
                continue
            else: break
        





    

def printWord(
    
    

            
            
        if currentWord in dict.keys():
            break
       

        
        print ' '
        print 'Current word fragment: ' + buildWord
        print 'Player 2\'s turn'
        buildWord2 = raw_input('Player 2 says letter:')
        print ' '
        print 'Current word fragment: ' + buildWord + buildWord2
        

string.ascii_lowercase



     

    
    
