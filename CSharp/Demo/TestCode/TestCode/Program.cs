/***********************************************************************************************************************
179. Largest Number: https://leetcode.com/problems/largest-number/
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer
Example 1: Input: nums = [10,2] Output: "210"
Example 2: Input: nums = [3,30,34,5,9] Output: "9534330"
Example 3: Input: nums = [1] Output: "1"
Example 4: Input: nums = [10] Output: "10"
***********************************************************************************************************************/

using System;
using System.Collections.Generic;

public static class Solution
{
    private static void Main()
    {
        var nums = new List<int> { 1, 12, 113 };
        var result = CalculateLargestString(nums);
        Console.WriteLine("Actual Result: " + result + ". Expected Result: " + "121131" + ". Test Passed: " + result.Equals("121131"));
        nums = new List<int> { 10, 2 };
        result = CalculateLargestString(nums);
        Console.WriteLine("Actual Result: " + result + ". Expected Result: " + "210" + ". Test Passed: " + result.Equals("210"));
        nums = new List<int> { 1, 2, 3, 4, 5 };
        result = CalculateLargestString(nums);
        Console.WriteLine("Actual Result: " + result + ". Expected Result: " + "54321" + ". Test Passed: " + result.Equals("54321"));
        nums = new List<int> { 3, 30, 34, 5, 9 };
        result = CalculateLargestString(nums);
        Console.WriteLine("Actual Result: " + result + ". Expected Result: " + "9534330" + ". Test Passed: " + result.Equals("9534330"));
        nums = new List<int> { 1 };
        result = CalculateLargestString(nums);
        Console.WriteLine("Actual Result: " + result + ". Expected Result: " + "1" + ". Test Passed: " + result.Equals("1"));
        nums = new List<int> { };
        result = CalculateLargestString(nums);
        Console.WriteLine("Actual Result: " + result + ". Expected Result: " + string.Empty + ". Test Passed: " + result.Equals(string.Empty));
    }

    private static string CalculateLargestString(List<int> nums)
    {
        string result = string.Empty;
        int max = 0;
        foreach (var num in nums)
        {
            max = Math.Max(max, num);
        }
        int maxDigits = max.ToString().Length;
        int highestNumber = 0;
        while (nums.Count > 0)
        {
            highestNumber = GetLargestNumberSortedByMostSignificatDigit(nums); // 113
            result += highestNumber.ToString();
            nums.Remove(highestNumber);
        }
        return result;
    }

    private static int GetLargestNumberSortedByMostSignificatDigit(List<int> nums)
    {
        var numbersWithHighestLastDigit = new List<int>();
        int highestNumberByLastDigit = 0;
        int highestLastDigit = 0;
        do
        {
            foreach (var num in nums)
            {
                highestLastDigit = Math.Max(highestLastDigit, num % 10);
            }
            foreach (var num in nums)
            {
                if (num % 10 == highestLastDigit)
                {
                    numbersWithHighestLastDigit.Add(num);
                }
            }
            foreach (var num in numbersWithHighestLastDigit)
            {
                highestNumberByLastDigit = Math.Max(highestNumberByLastDigit, num);
            }
        } while (numbersWithHighestLastDigit.Count > 1);

        return highestNumberByLastDigit;
    }
}