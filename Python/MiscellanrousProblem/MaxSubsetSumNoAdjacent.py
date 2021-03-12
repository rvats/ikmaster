def maxSubsetSumNoAdjacent(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	second = array[0]
	first = max(array[0], array[1])	
	for i in range(2, len(array)):
		second, first = first, max(first, second+array[i])
	return first