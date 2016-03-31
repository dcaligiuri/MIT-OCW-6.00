from string import*
def subStringMatchExact(target,key):
	hit = ()
	x = 0
	while (x<(len(target))):
                if (find(target,key,x+1) > find(target,key,x)):
                    hit = hit + (find(target,key,x),)
                elif (find(target,key,x+1) < find(target,key,x)):
                    hit = hit + (find(target,key,x),)
                x = x + 1
        return hit
