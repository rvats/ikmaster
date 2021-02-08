def arrayOfProducts(array):
	result = [1 for _ in range(len(array))]
	
	runningProduct = 1
	for i in range(len(array)):
		result[i]*=runningProduct
		runningProduct*=array[i]
	
	runningProduct = 1
	for i in reversed(range(len(array))):
		result[i]*=runningProduct
		runningProduct*=array[i]
		
	return result