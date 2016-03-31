def nestEggVariable(salary, save, growthRates):
	money = [salary*save*0.01]
	for x in range(0,len(growthRates)-1):
		money.append(money[x]*(1+0.01*growthRates[x+1]) + salary * save * 0.01)
	return money









        
