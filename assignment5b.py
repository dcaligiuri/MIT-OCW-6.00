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


            

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

