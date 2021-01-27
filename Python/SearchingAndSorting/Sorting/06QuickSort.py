class Sorting:
    # Bucket sort is mainly useful when input is uniformly distributed over a range. For example, consider the following problem.
    # Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range. How do we sort the numbers efficiently?
    # A simple way is to apply a comparison based sorting algorithm. The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(n Log n), i.e., they cannot do better than nLogn. Can we sort the array in linear time? Counting sort can not be applied here as we use keys as index in counting sort. Here keys are floating point numbers.
    # The idea is to use bucket sort. Following is bucket algorithm. bucketSort(arr[], n)
    # 1) Create n empty buckets (Or lists).
    # 2) Do following for every array element arr[i].
        # a) Insert arr[i] into bucket[n*array[i]]
    # 3) Sort individual buckets using insertion sort.
    # 4) Concatenate all sorted buckets.

    #@insertionSort
    def insertionSort(self, bucket): 
        for i in range(1, len(bucket)): 
            up = bucket[i] 
            j = i - 1
            while j >= 0 and bucket[j] > up:  
                bucket[j + 1] = bucket[j] 
                j -= 1
            bucket[j + 1] = up      
        return bucket      
              
    #@bucketSort
    def bucketSort(self, numbers): 
        bucket = [] 
        slot_num = len(numbers)-1 
        for i in range(slot_num): 
            bucket.append([]) 
          
        # Put array elements in different buckets  
        for j in numbers: 
            index_b = int(slot_num * j)  
            bucket[index_b].append(j) 
      
        # Sort individual buckets  
        for i in range(slot_num): 
            bucket[i] = self.insertionSort(bucket[i]) 
          
        # concatenate the result 
        k = 0
        for i in range(slot_num): 
            for j in range(len(bucket[i])): 
                numbers[k] = bucket[i][j] 
                k += 1
        return numbers

if __name__ == '__main__':
    print("Bucket Sort Demo")
    numbers = [0.897, 0.565, 0.656, 
     0.1234, 0.665, 0.3434] 
    print(Sorting().bucketSort(numbers))