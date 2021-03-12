def isValidSubsequence(array, sequence):
	sidx = 0
	#aidx = 0
	for i in range(len(array)):
		if array[i]==sequence[sidx]:
			sidx = sidx+1
		if sidx == len(sequence):
			return True
	return False

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))