using System;
using System.Collections.Generic;

public static class Solution
{
    private static void Main()
    {
        var nums = new int[] { 1, 12, 113 };
        Console.WriteLine(CalculateLargestString(nums));
        var nums = new int[] { 10, 2 };
        Console.WriteLine(CalculateLargestString(nums));
    }

    private static string CalculateLargestString(int[] nums)
    {
        Array.Sort(nums, (a, b) => (b + "" + a).CompareTo(a + "" + b));
        return nums[0] == 0 ? "0" : string.Join("", nums);
    }
}