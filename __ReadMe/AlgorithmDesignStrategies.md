What is an algorithm? 
An Algorithm is a procedure to solve a particular problem in a finite number of steps for a finite-sized input. 
The algorithms can be classified in various ways. They are: 
Implementation Method
Design Method
Other Classifications

Classification by Implementation Method: There are primarily three main categories into which an algorithm can be named in this type of classification. They are:
Recursion or Iteration: A recursive algorithm is an algorithm which calls itself again and again until a base condition is achieved whereas iterative algorithms use loops and/or data structures like stacks, queues to solve any problem. Every recursive solution can be implemented as an iterative solution and vice versa. 
Example: The Tower of Benaras -Hanoi- is implemented in a recursive fashion while Stock Span problem is implemented iteratively.
Exact or Approximate: Algorithms that are capable of finding an optimal solution for any problem are known as the exact algorithm. For all those problems, where it is not possible to find the most optimized solution, an approximation algorithm is used. Approximate algorithms are the type of algorithms that find the result as an average outcome of sub outcomes to a problem. 
Example: For NP-Hard Problems, approximation algorithms are used. Sorting algorithms are the exact algorithms.
Serial or Parallel or Distributed Algorithms: In serial algorithms, one instruction is executed at a time while parallel algorithms are those in which we divide the problem into subproblems and execute them on different processors. If parallel algorithms are distributed on different machines, then they are known as distributed algorithms.


Classification by Design Method: There are primarily three main categories into which an algorithm can be named in this type of classification. They are: 
Greedy Method: In the greedy method, at each step, a decision is made to choose the local optimum, without thinking about the future consequences.
Example: Fractional Knapsack, Activity Selection.
Divide and Conquer: The Divide and Conquer strategy involves dividing the problem into sub-problem, recursively solving them, and then recombining them for the final answer. 
Example: Merge sort, Quicksort.
Dynamic Programming: The approach of Dynamic programming is similar to divide and conquer. The difference is that whenever we have recursive function calls with the same result, instead of calling them again we try to store the result in a data structure in the form of a table and retrieve the results from the table. Thus, the overall time complexity is reduced. “Dynamic” means we dynamically decide, whether to call a function or retrieve values from the table. 
Example: 0-1 Knapsack, subset-sum problem.
Linear Programming: In Linear Programming, there are inequalities in terms of inputs and maximizing or minimizing some linear functions of inputs.
Example: Maximum flow of Directed Graph
Reduction(Transform and Conquer): In this method, we solve a difficult problem by transforming it into a known problem for which we have an optimal solution. Basically, the goal is to find a reducing algorithm whose complexity is not dominated by the resulting reduced algorithms. 
Example: Selection algorithm for finding the median in a list involves first sorting the list and then finding out the middle element in the sorted list. These techniques are also called transform and conquer.

Other Classifications: Apart from classifying the algorithms into the above broad categories, the algorithm can be classified into other broad categories like: 
 

Randomized Algorithms: Algorithms that make random choices for faster solutions are known as randomized algorithms. 
Example: Randomized Quicksort Algorithm.
Classification by complexity: Algorithms that are classified on the basis of time taken to get a solution to any problem for input size. This analysis is known as time complexity analysis. 
Example: Some algorithms take O(n), while some take exponential time.
Classification by Research Area: In CS each field has its own problems and needs efficient algorithms. 
Example: Sorting Algorithm, Searching Algorithm, Machine Learning etc.
Branch and Bound Enumeration and Backtracking: These are mostly used in Artificial Intelligence.