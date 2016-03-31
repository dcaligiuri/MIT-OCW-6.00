def constrainedMatchPair(firstMatch,secondMatch,length):
	m = length
	nearHits = ()
	for n in range(0,len(firstMatch)):
		n = firstMatch[n]
		for k in range(0,len(secondMatch)):
			k = secondMatch[k]
			if n + m + 1 == k:
				nearHits = nearHits + (n,)
	return nearHits

