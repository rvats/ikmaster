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
'''
# Fibonacci Series No Optimization
# Time Complexity = O(n) Space Complexity = O(n)
def fibonacciNaive(number):
    if number <= 2:
        return 1
    else:
        return fibonacciNaive(number-1) + fibonacciNaive(number-2)

print(fibonacciNaive(25))

# Fibonacci Series using Dynamic Programming using Memoization 1
# Time Complexity = O(n) Space Complexity = O(n)
def fibonacci_memo(number):
    if number in fibonacci_cache:
        return fibonacci_cache[number]
    if number <= 2:
        return 1
    else:           
        value =  fibonacci_memo(number-1) + fibonacci_memo(number-2)
    fibonacci_cache[number] = value
    return value

# Fibonacci Series using Dynamic Programming using Memoization 2
# Time Complexity = O(n) Space Complexity = O(n)
@lru_cache(maxsize = 1000)
def fibonacci_cache(number):
    if number <= 2:
        return 1
    else:
        return fibonacci_cache(number-1) + fibonacci_cache(number-2)
for i in range(1, 201):
     print("fibonacci({}) = ".format(i), fibonacci_cache(i))

# Fibonacci Series using Dynamic Programming using Memoization 3
# Time Complexity = O(n)
def fibonacci(n):  
    # Taking 1st two fibonacci nubers as 0 and 1  
    f = [0, 1, 1]  
    for i in range(3, n+1): 
        f.append(f[i-1] + f[i-2]) 
    return f 
for index,number in enumerate(fibonacci(100)):
    print("fibonacci({}) = ".format(index), number)