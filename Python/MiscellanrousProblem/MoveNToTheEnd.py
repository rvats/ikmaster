def moveElementToEnd(array, toMove):
	left, right = 0, len(array)-1
	while left < right:
		if array[left] == toMove and array[right] != toMove:
			array[left], array[right] = array[right], array[left]
			left+=1
			right-=1
		elif array[left] != toMove: 
			left+=1
		elif array[right] == toMove:
			right-=1
	return array

array= [2,1,2,3,2,4,2]
print(moveElementToEnd(array,2))
array= [1,1,1,3,2,4,2]
print(moveElementToEnd(array,1))