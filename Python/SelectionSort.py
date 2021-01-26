class Sorting:
    # The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning (You can also do by finding the max element and putting in the end for asc and at the beginning for descending sort). The algorithm maintains two subarrays in a given array.
    # 1) The subarray which is already sorted.
    # 2) Remaining subarray which is unsorted.
    # In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

    #@selectionSort1 self, nums):
    def selectionSort1(self, numbers):
        for i in range(len(numbers)): 
            # Find the minimum element in remaining  
            # unsorted array 
            min_idx = i 
            for j in range(i+1, len(numbers)): 
                if numbers[min_idx] > numbers[j]: 
                    min_idx = j       
            # Swap the found minimum element with  
            # the first element         
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i] 
        return numbers

    # @selectionSort2, TLE
    def selectionSort2(self, numbers):
        for i in range(len(numbers)): # O(n)
            _min = min(numbers[i:]) # Combining the second for loop into a min function call Time Complexity is still O(n)
            min_index = numbers[i:].index(_min)
            numbers[i + min_index] = numbers[i]
            numbers[i] = _min
        return numbers

if __name__ == '__main__':
    print(Sorting().selectionSort1([5,4,3,2,1]))
    print(Sorting().selectionSort2([5,4,3,2,1]))