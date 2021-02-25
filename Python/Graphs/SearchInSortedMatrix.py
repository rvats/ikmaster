def searchInSortedMatrix(matrix, target):
	for row in range(len(matrix)):
		result = binarySearch(row, matrix[row], target)
		if result != [-1,-1]:
			return result
	return[-1,-1]
	
def binarySearch(row, array, target):
	start, end = 0, len(array)-1
	while start <= end:
		mid = start+(end-start)//2
		if array[mid] == target:
			return [row, mid]
		elif array[mid] > target:
			end = mid-1
		elif array[mid] < target:
			start = mid+1
	return [-1,-1]

matrix = [
	[ 1,   4,   7,  12,  15, 1000],
	[ 2,   5,  19,  31,  32, 1001],
	[ 3,   8,  24,  33,  35, 1002],
	[40,  41,  42,  44,  45, 1003],
	[99, 100, 103, 106, 128, 1004]
]
print(searchInSortedMatrix(matrix,1004))