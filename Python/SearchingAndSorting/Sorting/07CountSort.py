class Sorting:
    # Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.
    # Let us understand it with the help of an example. 
    # For simplicity, consider the data in the range 0 to 9. 
    # Input data: 1, 4, 1, 2, 7, 5, 2
    # 1) Take a count array to store the count of each unique object.
    # Index:     0  1  2  3  4  5  6  7  8  9
    # Count:     0  2  2  0   1  1  0  1  0  0
    # 2) Modify the count array such that each element at each index to store the sum of previous counts. 
    # Index:     0  1  2  3  4  5  6  7  8  9
    # Count:     0  2  4  4  5  6  6  7  7  7
    # The modified count array indicates the position of each object in the output sequence.
    # 3) Output each object from the input sequence followed by decreasing its count by 1.
    # Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2.
    # Put data 1 at index 2 in output. Decrease count by 1 to place next data 1 at an index 1 smaller than this index.

    #@countSort
    def countSort(self, numbers):
        max_element = int(max(numbers))
        min_element = int(min(numbers))
        range_of_elements = max_element - min_element + 1
        # Create a count array to store count of individual
        # elements and initialize count array as 0
        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(len(numbers))]
 
        # Store count of each character
        for i in range(0, len(numbers)):
            count_arr[numbers[i]-min_element] += 1
 
        # Change count_arr[i] so that count_arr[i] now contains actual
        # position of this element in output array
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]
 
        # Build the output character array
        for i in range(len(numbers)-1, -1, -1):
            output_arr[count_arr[numbers[i] - min_element] - 1] = numbers[i]
            count_arr[numbers[i] - min_element] -= 1
 
        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(0, len(numbers)):
            numbers[i] = output_arr[i]

        return numbers

if __name__ == '__main__':
    print("Count Sort Demo")
    numbers = [9,8,7,6,5,4,3,2,1,0] 
    print(Sorting().countSort(numbers))