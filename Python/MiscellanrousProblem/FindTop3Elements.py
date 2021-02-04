def findThreeLargestNumbersMine(array):
	current3Max = float('-inf')
	max3Map = []
	for num in array:
		if len(max3Map) < 3:
			current3Max = min(current3Max,num)
			max3Map.append(num)
		else:
			current3Max = max(current3Max,num)
			for i in range(3):
				if current3Max > max3Map[i]:
					current3Max, max3Map[i] = max3Map[i], current3Max
	max3Map.sort()
	return max3Map


def findThreeLargestNumbers(array):
	threeLargest = [None, None, None]
	for num in array: 
		updateLargest (threeLargest, num)
	return threeLargest

def updateLargest(threeLargest, num):
	if threeLargest[2] is None or num > threeLargest[2]:
		shiftAndUpdate(threeLargest, num, 2)
	elif threeLargest[1] is None or num > threeLargest[1]:
		shiftAndUpdate(threeLargest, num, 1)
	elif threeLargest[0] is None or num > threeLargest[0]:
		shiftAndUpdate(threeLargest, num, 0)
		
def shiftAndUpdate(array, num, idx):
	for i in range(idx+1):
		if i == idx:
			array[i]=num
		else:
			array[i] = array[i+1]

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 600]

print(findThreeLargestNumbers(array))