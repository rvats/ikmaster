class Sorting:
    # Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
    # Algorithm
    # To sort an array of size n in ascending order:
    # 1: Iterate from arr[1] to arr[n] over the array.
    # 2: Compare the current element (key) to its predecessor.
    # 3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

    #@insertionSort
    def insertionSort(self, numbers): 
        for i in range(1, len(numbers)): 
            up = numbers[i] 
            j = i - 1
            while j >= 0 and numbers[j] > up:  
                numbers[j + 1] = numbers[j] 
                j -= 1
            numbers[j + 1] = up      
        return numbers

if __name__ == '__main__':
    print("Insertion Sort Demo")
    numbers = [897, 565, 656, 1234, 665, 3434] 
    print(Sorting().insertionSort(numbers))