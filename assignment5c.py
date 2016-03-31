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


