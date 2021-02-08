def longestPeak(array):
	longestPeakLength = 0
	idx = 1
	while idx < len(array) - 1:
		isPeak = array[idx-1] < array[idx] and array[idx] > array[idx+1]
		if not isPeak:
			idx+=1
			continue
		
		left = idx-2
		while left >=0 and array[left] < array[left+1]:
			left-=1
		right = idx+2
		while right < len(array) and array[right] < array [right-1]:
			right+=1
		
		currentPeakLength = right-left-1
		longestPeakLength = max(longestPeakLength, currentPeakLength)
		idx = right
	return longestPeakLength

