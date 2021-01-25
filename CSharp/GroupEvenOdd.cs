using System;

public class GroupEvenOdd
{
    public static void Main()
    {
        var numbers = GroupEvenOdd(new int[] { 2, 4, 6, 1, 3, 5 });
        foreach (int number in numbers)
        {
            Console.WriteLine(number);
        }
        numbers = GroupEvenOdd(new int[] { 1, 2, 3, 4, 5, 6 });
        foreach (int number in numbers)
        {
            Console.WriteLine(number);
        }
        numbers = GroupEvenOdd(new int[] { 1, 3, 5, 2, 4, 6 });
        foreach (int number in numbers)
        {
            Console.WriteLine(number);
        }
    }

    static int[] GroupEvenOdd(int[] arr)
    {
        // variables
        int j = -1, temp;

        // quick sort method
        for (int i = 0; i < arr.Length; i++)
        {

            // if array of element
            // is even then swap
            if (arr[i] % 2 == 0)
            {

                // increment j by one
                j++;
                Console.WriteLine(string.Format("{0} {1} {2} {3}", i, j, arr[i], arr[j]));
                // swap the element
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        return arr;
    }
}