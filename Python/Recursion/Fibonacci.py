from functools import lru_cache
'''
Dynamic programming problems can be solved using either bottom-up or top-down approaches.
Generally, the bottom-up approach uses the tabulation technique, while the top-down approach uses the recursion (with memorization) technique.
But you can also have bottom-up and top-down approaches using recursion as shown below.
Bottom-Up: Start with the base condition and pass the value calculated until now recursively. Generally, these are tail recursions.
int n = 5;
fibBottomUp(1, 1, 2, n);
private int fibBottomUp(int i, int j, int count, int n) {
    if (count > n) return 1;
    if (count == n) return i + j;
    return fibBottomUp(j, i + j, count + 1, n);
}
Top-Down: Start with the final condition and recursively get the result of its sub-problems.
int n = 5;
fibTopDown(n);

private int fibTopDown(int n) {
    if (n <= 1) return 1;
    return fibTopDown(n - 1) + fibTopDown(n - 2);
}
Resources: 
https://towardsdatascience.com/memoization-in-python-57c0a738179a
'''
# Fibonacci Series No Optimization
# Time Complexity = O(n^2) Space Complexity = O(1)
def fibonacciNaive(number):
    if number <= 2:
        return 1
    else:
        return fibonacciNaive(number-1) + fibonacciNaive(number-2)
for i in range(1, 36):
     print("fibonacciNaive({}) = ".format(i), fibonacciNaive(i))


fibonacci_cache = {}
# Fibonacci Series using Dynamic Programming using Memoization 1
# Time Complexity = O(n) Space Complexity = O(n)
def fibonacciMemo(number):
    if number in fibonacci_cache:
        return fibonacci_cache[number]
    if number <= 2:
        return 1
    else:           
        value =  fibonacciMemo(number-1) + fibonacciMemo(number-2)
    fibonacci_cache[number] = value
    return value
for i in range(1, 1003):
     print("fibonacciMemo({}) = ".format(i), fibonacciMemo(i))

# Fibonacci Series using Dynamic Programming using Memoization 2
# Time Complexity = O(n) Space Complexity = O(n)
@lru_cache(maxsize = 1003)
def fibonacciCache(number):
    if number <= 2:
        return 1
    else:
        return fibonacciCache(number-1) + fibonacciCache(number-2)
for i in range(1, 1003):
     print("fibonacciCache({}) = ".format(i), fibonacciCache(i))

# Fibonacci Series using Iterative Approach using Tabularization 3
# Time Complexity = O(n)
def fibonacciIterative(n):  
    # Taking 1st two fibonacci nubers as 0 and 1  
    f = [0, 1, 1]  
    for i in range(3, n+1): 
        f.append(f[i-1] + f[i-2]) 
    return f 
for index,number in enumerate(fibonacciIterative(1003)):
    print("fibonacciIterative({}) = ".format(index), number)