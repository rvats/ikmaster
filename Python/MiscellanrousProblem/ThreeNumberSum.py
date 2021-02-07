def threeNumberSum(array, targetSum):
	array.sort()
	triplets = []
	for idx in range(len(array)-2):
		left = idx+1
		right = len(array)-1
		while(left < right):
			currentSum = array[idx]+array[left]+array[right]
			if currentSum == targetSum:
				triplets.append([array[idx],array[left],array[right]])
				left+=1
				right-=1
			elif currentSum < targetSum:
				left+=1
			elif currentSum > targetSum:
				right-=1
	return triplets