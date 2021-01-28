using System;

public static class Solution
{
    private static void Main()
    {
        var nums = new int[] { 1, 12, 113 };
        Console.WriteLine(CalculateLargestString(nums));
        nums = new int[] { 10, 2 };
        Console.WriteLine(CalculateLargestString(nums));
        nums = new int[] { 1, 2, 3, 4, 5 };
        Console.WriteLine(CalculateLargestString(nums));
    }

    private static string CalculateLargestString(int[] nums)
    {
        Array.Sort(nums, (a, b) => (b + "" + a).CompareTo(a + "" + b));
        foreach (var num in nums) {
            Console.WriteLine(num);
        }
        return nums[0] == 0 ? "0" : string.Join("", nums);
    }
}