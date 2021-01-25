using System;
using System.Collections.Generic;

public class SortDutchFlag
{
    public static void Main()
    {
        var list = new List<char> { 'B', 'R', 'G' };
        SortDutchFlag(list);

        list = new List<char> { 'B', 'R', 'G', 'B', 'B', 'R', 'G', 'B', 'R', 'G' };
        SortDutchFlag(list);

        list = new List<char> { 'R', 'R', 'R', 'R', 'G', 'G', 'G', 'G', 'B', 'B', 'B', 'B' };
        SortDutchFlag(list);
    }

    public static void SortDutchFlag(List<char> balls)
    {
        PrintBalls(balls);
        var low = 0;
        var mid = 0;
        var high = balls.Count - 1;

        // one pass through the array swapping
        // the necessary elements in place
        while (mid <= high)
        {
            if (balls[mid] == 'R')
            {
                Swap(balls, low++, mid++);
            }
            else if (balls[mid] == 'G')
            {
                mid++;
            }
            else if (balls[mid] == 'B')
            {
                Swap(balls, mid, high--);
            }
        }

        PrintBalls(balls);
    }

    public static void Swap(List<char> balls, int i1, int i2)
    {
        Console.WriteLine(balls[i1].ToString() + " " + balls[i2]);
        var temp = balls[i1];
        balls[i1] = balls[i2];
        balls[i2] = temp;
    }

    public static void PrintBalls(List<char> balls)
    {
        foreach (var ball in balls)
        {
            Console.Write(ball);
        }
        Console.WriteLine();
    }
}