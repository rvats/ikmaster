def numberOfWaysToMakeChange(n, denoms):
	def helper(target, ways=0):
		print(target, ways)
		if target == 0:
			ways+=1
		else:
			for num in denoms:
				if target-num>=0:
					ways=helper(target-num, ways)
		return ways
	ways = helper(n, 0)
	return ways - 1

print(numberOfWaysToMakeChange(6,[1,5]))