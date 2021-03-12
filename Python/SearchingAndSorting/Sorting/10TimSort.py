import random
class Sorting:
    # TimSort is a sorting algorithm based on Insertion Sort and Merge Sort.
    # A stable sorting algorithm works in O(n Log n) time
    # Used in Java’s Arrays.sort() as well as Python’s sorted() and sort().
    # First sort small pieces using Insertion Sort, then merges the pieces using merge of merge sort.
    # We divide the Array into blocks known as Run. We sort those runs using insertion sort one by one and then merge those runs using the combine function used in merge sort. If the size of the Array is less than run, then Array gets sorted just by using Insertion Sort. The size of the run may vary from 32 to 64 depending upon the size of the array. Note that the merge function performs well when size subarrays are powers of 2. The idea is based on the fact that insertion sort performs well for small arrays.

    # Python3 program to perform basic timSort 
    MIN_MERGE = 32

    #@calcMinRun
    def calcMinRun(self, n): 
        """Returns the minimum length of a  
        run from 23 - 64 so that 
        the len(array)/minrun is less than or  
        equal to a power of 2. 
  
        e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,  
        ..., 127=>64, 128=>32, ... 
        """
        r = 0
        while n >= self.MIN_MERGE: 
            r |= n & 1
            n >>= 1
        return n + r

    #@insertionSort
    # This function sorts array from left index to 
    # to right index which is of size atmost RUN 
    def insertionSort(self, arr, left, right): 
        for i in range(left + 1, right + 1): 
            j = i 
            while j > left and arr[j] < arr[j - 1]: 
                arr[j], arr[j - 1] = arr[j - 1], arr[j] 
                j -= 1
    
    #@insertionSort
    # Merge function merges the sorted runs 
    def merge(self, arr, l, m, r): 
      
        # original array is broken in two parts 
        # left and right array 
        len1, len2 = m - l + 1, r - m 
        left, right = [], [] 
        for i in range(0, len1): 
            left.append(arr[l + i]) 
        for i in range(0, len2): 
            right.append(arr[m + 1 + i]) 
  
        i, j, k = 0, 0, l 
      
        # after comparing, we merge those two array 
        # in larger sub array 
        while i < len1 and j < len2: 
            if left[i] <= right[j]: 
                arr[k] = left[i] 
                i += 1
  
            else: 
                arr[k] = right[j] 
                j += 1
  
            k += 1
  
        # Copy remaining elements of left, if any 
        while i < len1: 
            arr[k] = left[i] 
            k += 1
            i += 1
  
        # Copy remaining element of right, if any 
        while j < len2: 
            arr[k] = right[j] 
            k += 1
            j += 1

    #@timSort
    # Iterative Timsort function to sort the 
    # array[0...n-1] (similar to merge sort) 
    def timSort(self, arr): 
        n = len(arr) 
        minRun = self.calcMinRun(n) 
      
        # Sort individual subarrays of size RUN 
        for start in range(0, n, minRun): 
            end = min(start + minRun - 1, n - 1) 
            self.insertionSort(arr, start, end) 
  
        # Start merging from size RUN (or 32). It will merge 
        # to form size 64, then 128, 256 and so on .... 
        size = minRun 
        while size < n: 
          
            # Pick starting point of left sub array. We 
            # are going to merge arr[left..left+size-1] 
            # and arr[left+size, left+2*size-1] 
            # After every merge, we increase left by 2*size 
            for left in range(0, n, 2 * size): 
  
                # Find ending point of left sub array 
                # mid+1 is starting point of right sub array 
                mid = min(n - 1, left + size - 1) 
                right = min((left + 2 * size - 1), (n - 1)) 
  
                # Merge sub array arr[left.....mid] & 
                # arr[mid+1....right] 
                self.merge(arr, left, mid, right) 
  
            size = 2 * size
        return arr

if __name__ == '__main__':
    print("Tim Sort Demo")
    numbers = []
    for _ in range(64):
        n = random.randint(1000,99999) # whatever your range of random numbers is
        numbers.append(n)
    print("Numbers before Sorting: ")
    print(numbers)
    print("Numbers after Sorting: ")
    print(Sorting().timSort(numbers))