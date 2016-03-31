def nestEggFixed(salary,save,growthRate,years):
	money = [salary*save*0.01]
	for x in range(0,years-1):
		money.append(money[x]*(1+0.01*growthRate) + salary * save * 0.01)
	return money
