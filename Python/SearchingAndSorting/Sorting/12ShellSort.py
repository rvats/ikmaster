import random
class Sorting:
    # ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved. The idea of shellSort is to allow exchange of far items. In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all sublists of every h’th element is sorted.

    #@shellSort
    def shellSort(self, arr): 
        # Start with a big gap, then reduce the gap 
        n = len(arr) 
        gap = n//2
  
        # Do a gapped insertion sort for this gap size. 
        # The first gap elements a[0..gap-1] are already in gapped  
        # order keep adding one more element until the entire array 
        # is gap sorted 
        while gap > 0: 
  
            for i in range(gap,n): 
  
                # add a[i] to the elements that have been gap sorted 
                # save a[i] in temp and make a hole at position i 
                temp = arr[i] 
  
                # shift earlier gap-sorted elements up until the correct 
                # location for a[i] is found 
                j = i 
                while  j >= gap and arr[j-gap] >temp: 
                    arr[j] = arr[j-gap] 
                    j -= gap 
  
                # put temp (the original a[i]) in its correct location 
                arr[j] = temp 
            gap //= 2
        return arr

if __name__ == '__main__':
    print("Shell Sort Demo")
    numbers = []
    for _ in range(10):
        n = random.randint(0,100) # whatever your range of random numbers is
        numbers.append(n)
    print("Numbers before Sorting: ")
    print(numbers)
    print("Numbers after Sorting: ")
    print(Sorting().shellSort(numbers))