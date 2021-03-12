def twoNumberSum(array, targetSum):
	sumMap = {}
	output = []
	for i in range(len(array)):
		if array[i] in sumMap:
			return [array[i], sumMap[array[i]]]
		else:
			sumMap[targetSum-array[i]] = array[i]
	return [-1,-1]

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10))