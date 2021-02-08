def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	s1, s2 = 0, 0
	smallestDiff = float("inf")
	currentDiff = float("inf")
	result = []
	while (s1<len(arrayOne) and s2<len(arrayTwo)):
		smallestDiff = min(smallestDiff,currentDiff)
		currentDiff = abs(arrayOne[s1]-arrayTwo[s2])
		if currentDiff < smallestDiff:
			result = [arrayOne[s1],arrayTwo[s2]]
		if currentDiff == 0:
			return result
		elif arrayOne[s1]<arrayTwo[s2]:
			s1+=1
		elif arrayTwo[s2]<arrayOne[s1]:
			s2+=1
	return result


arrayOne = [10,0,20,25,2200]
arrayTwo = [1005,1006,1014,1032,1031]
print(smallestDifference(arrayOne,arrayTwo))
arrayOne = [10,1000,9124,2142,59,24,596,591,124,-123]
arrayTwo = [-1441,-124,-25,1014,1500,660,410,245,530]
print(smallestDifference(arrayOne,arrayTwo))

