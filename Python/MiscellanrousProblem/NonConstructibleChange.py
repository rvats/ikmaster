def nonConstructibleChange(coins):
	coins.sort()
	currentChangeCreated = 0
	for coin in coins:
		if coin > currentChangeCreated+1:
			return currentChangeCreated+1
		currentChangeCreated+=coin
	return currentChangeCreated+1

print(nonConstructibleChange([5, 3, 1, 2, 1, 7, 22]))
print(nonConstructibleChange([5, 3, 1, 2, 5, 7, 22]))