# imports random
import random
class Sorting:
    def quickSort(self, numbers, low, high):
        if (low < high):
            pi, pj = self.partition(numbers, low, high)
            self.quickSort(numbers, low, pi - 1)
            self.quickSort(numbers, pj + 1, high)

    def partition(self, numbers, low, high): 
        i = ( low-1 )
        pivot = numbers[high]
        j = low
        while j < high: 
            if numbers[j] < pivot: 
                i = i+1 
                numbers[i],numbers[j] = numbers[j],numbers[i]
            if numbers[j] == pivot: 
                i = i+1 
                numbers[i],numbers[j] = numbers[j],numbers[i] 
        numbers[i+1],numbers[high] = numbers[high],numbers[i+1] 
        return ( i+1, j+1 ) 

if __name__ == '__main__':
    print("Quick Sort Demo")
    numbers = [8971, 8971, 8971, 9565, 9565, 9565, 8656, 8656, 1234, 1234, 665, 665, 3434, 3434, 3434] 
    Sorting().quickSort(numbers,0,len(numbers)-1)
    print(numbers)