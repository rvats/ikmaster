class Sorting:
    # Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See the following C implementation for details.
    # MergeSort(arr[], l,  r)
    # If r > l
    # 1. Find the middle point to divide the array into two halves:   middle m = (l+r)/2
    # 2. Call mergeSort for first half:   Call mergeSort(arr, l, m)
    # 3. Call mergeSort for second half:   Call mergeSort(arr, m+1, r)
    # 4. Merge the two halves sorted in step 2 and 3:   Call merge(arr, l, m, r)

    #@insertionSort
    def mergeSort(self, numbers): 
        if len(numbers) > 1:
            # Finding the mid of the array
            mid = len(numbers)//2
            # Dividing the array elements
            L = numbers[:mid]
            # into 2 halves
            R = numbers[mid:]
            # Sorting the first half
            self.mergeSort(L) 
            # Sorting the second half
            self.mergeSort(R) 
            i = j = k = 0 
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    numbers[k] = L[i]
                    i += 1
                else:
                    numbers[k] = R[j]
                    j += 1
                k += 1
            # Checking if any element was left
            while i < len(L):
                numbers[k] = L[i]
                i += 1
                k += 1 
            while j < len(R):
                numbers[k] = R[j]
                j += 1
                k += 1
            return numbers

if __name__ == '__main__':
    print("Merge Sort Demo")
    numbers = [897, 565, 656, 1234, 665, 3434] 
    print(Sorting().mergeSort(numbers))