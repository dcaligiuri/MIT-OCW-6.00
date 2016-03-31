from string import*
def countSubStringMatch(target,key):
    for x in range(0,len(target)):
	count = 0
	if find(target,key,x) >= 0:
	    count = count + 1
    
    
 
