def isMonotonic(array):
	hasChecked = False
	isIncreasing = False
	if len(array) <= 1:
		return True
	else:
		for idx in range(len(array)-1):
			if array[idx] < array[idx+1] and not hasChecked:
				isIncreasing = True
				hasChecked = True
			elif array[idx] > array[idx+1] and not hasChecked:
				hasChecked = True
			elif hasChecked and isIncreasing and array[idx] > array[idx+1]:
				return False
			elif hasChecked and not isIncreasing and array[idx] < array[idx+1]:
				return False
	return True

array = [1,2,0]
print(isMonotonic(array))