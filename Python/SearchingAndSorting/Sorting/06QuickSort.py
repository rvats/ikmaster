# imports random
import random
class Sorting:
    # Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.
    # Always pick first element as pivot.
    # Always pick last element as pivot (implemented below)
    # Pick a random element as pivot.
    # Pick median as pivot.
    # The key process in quickSort is partition(). 
    # /* low  --> Starting index,  high  --> Ending index */
    # quickSort(numbers[], low, high):
    #   if (low < high)
    #   /* pi is partitioning index, numbers[pi] is now at right place */
    #       pi = partition(numbers, low, high);
    #       quickSort(numbers, low, pi - 1);  // Before pi
    #       quickSort(numbers, pi + 1, high); // After pi

    #@quickSort
    def quickSort(self, numbers, low, high):
        if (low < high):
            pi = self.partition(numbers, low, high)
            self.quickSort(numbers, low, pi - 1)
            self.quickSort(numbers, pi + 1, high)

    # This function takes last element as pivot, places 
    # the pivot element at its correct position in sorted 
    # array, and places all smaller (smaller than pivot) 
    # to left of pivot and all greater elements to right 
    # of pivot 
    def partition(self, numbers, low, high): 
        i = ( low-1 )         # index of smaller element 
        # randint generates a random integar between the first parameter and the second
        pivot = numbers[high]     # pivot random.randint(low, high)
        for j in range(low , high): 
            # If current element is smaller than the pivot 
            if numbers[j] < pivot: 
                # increment index of smaller element 
                i = i+1 
                numbers[i],numbers[j] = numbers[j],numbers[i] 
        numbers[i+1],numbers[high] = numbers[high],numbers[i+1] 
        return ( i+1 ) 

if __name__ == '__main__':
    print("Quick Sort Demo")
    numbers = [8971, 9565, 8656, 1234, 665, 3434] 
    Sorting().quickSort(numbers,0,len(numbers)-1)
    print(numbers)