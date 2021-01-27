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

    # An optimized version of Bubble Sort 
    def bubbleSortOptimized(self, numbers): 
        n = len(numbers) 
   
        # Traverse through all array elements 
        for i in range(n): 
            swapped = False
  
            # Last i elements are already 
            #  in place 
            for j in range(0, n-i-1): 
   
                # traverse the array from 0 to 
                # n-i-1. Swap if the element  
                # found is greater than the 
                # next element 
                if numbers[j] > numbers[j+1] : 
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j] 
                    swapped = True
  
            # IF no two elements were swapped 
            # by inner loop, then break 
            if swapped == False: 
                break
        return numbers

if __name__ == '__main__':
    print("Bubble Sort Demo")
    print(Sorting().bubbleSort([5,4,3,2,1]))
    print(Sorting().bubbleSortOptimized([5,4,3,2,1]))