class Sorting:
    # Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

    #@bubbleSort, TLE
    def bubbleSort(self, numbers):
        n = len(numbers) 
        # Traverse through all array elements 
        for i in range(n): 
            # Last i elements are already in place
            for j in range(0, n-i-1): 
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if numbers[j] > numbers[j+1] : 
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers

if __name__ == '__main__':
    print(Sorting().bubbleSort([5,4,3,2,1]))