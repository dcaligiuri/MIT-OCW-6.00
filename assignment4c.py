def postRetirement(savings, growthRates, expenses):
        money = [savings * (1 + 0.01 * growthRates[0]) - expenses]
        for x in range(0,len(growthRates)-1):
            money.append(money[x]*(1+ 0.01 * growthRates[x+1]) - expenses)
	return money
