'''
What expressions are there to consider?
There are n digits so n-1 positions between those digits to insert operations. 
We can insert one of the three operations in any of the n-1 positions. So there are a total of 3^(n-1) distinct expressions we need to care about.
Do we have to consider all 3^(n-1) expressions or can we exclude some?
While it is possible to skip _some_ expressions sometimes (e.g. if target=4, any expressions beginning with "5+" aren't worth considering), it won't make the worst case any better. As such, let's simply consider all the expressions.
How can we generate all those expressions?
Imagine that we call a function with a specific expression already made out of several first digits from s, e.g. func("1+3"). That invocation could then make 3 calls of the same function appending the next digit from s in 3 different ways: func("1+34"), func("1+3*4"), func("1+3+4"). That way every subsequent/nested call of the recursive function would add one digit. When all the digits from s have been used up (that would be the base condition for the recursion), instead of calling itself again, the function would check if the expression built so far evaluates to the target.
Should we store all the generated expressions in memory first? (then evaluate them one by one and compare their values to the target)
Or should we evaluate every expression immediately once it's built and only store it if it evaluates to the target?
Or should we evaluate the expressions incrementally, as we build them? (then by the time all digits from s have been used up, we are also done evaluating the expression; we can compare it to the target)
Any of these strategies would work;
How do we evaluate the expressions?
Evaluating arithmetic expressions is a subject of its own, a class of algorithms. Generally, an expression is first converted from the conventional ("infix") notation one of the more convenient notations (e.g. "postfix"); second stage then calculates the numeric value from that other notation. Maintaining the precedence of operations is key in both processes and stack data structure is generally utilized.
While using an approach like that is an option, we can get away with something a little bit simpler because we only really have two operations: "+" and "*". Here is one trick that optimal_solution.cpp uses. Let’s say s="123". How would we build expression "1+2*3", digit by digit, and evaluate its value as we go?
We would first have expression "1" and its value 1.
Appending "+2" we would get "1+2" and the value would be easy to calculate, 1+2=3.
What happens when we append "*3"? Now "2" has to be multiplied, not added. How can we get the value of the new expression "1+2*3" from the value of "1+2" that we already have?
Take the value of the sub-expression after the last "+" in "1+2", that's 2.
Subtract that from the value of the previous expression, 3-2=1.
Perform the multiplication we have to perform, 2*3=6.
Finally, add up the last two results, 1+6=7.
Time Complexity:
Let us find 1) the time complexity of one invocation of the recursive function generate_all_expressions_util() and 2) the number of those invocations. Multiplying (1) by (2) we will find the time complexity of the algorithm.
One invocation takes O(n) time: it calls functions substr(), str_to_ll() on strings of length O(n), it copies and concatenates strings -- any of them (as well as all of them combined) takes O(n) time.
How many recursive invocations are made?
Drawing the recursion tree is one way to find out. Drawing just 3-4 levels of it, you may start noticing that every recursive call represents a distinct expression made of k digits (for every k from 1 to n), the value of cur_expr parameter is that expression. Exactly one call is made for every possible expression and no other calls are made. (The first/root call with cur_expr=="" is an exception but that's insignificant asymptotically)
Let us try to count those calls. We won't group them by level in the recursion tree (as that's usually done) but by number of digits in the expression:
there are 3^(n-1) distinct expressions made of n digits (as we established in the very beginning)
3^(n-2) expressions made of n-1 digits
3^1=3 expressions made of 2 digits
3^0=1 expression made of 1 digit
The above are the first n terms of the geometric series with first element a1=1 and ratio r=3. Their sum:
Sn = (a1*(1-r^n))/(1-r) = (1*(1-3^n))/(1-3) = (3^n)/2 - ½
We could add 1 for the root recursive call to get exact number of nodes in the recursion tree, but asymptotically that won't matter.
Overall we have O(3^n) recursive calls each taking O(n) time.
Total time complexity is O(n*3^n).
Auxiliary Space Used:
Space is used for the recursive stack frames as well as for the expressions (strings) collected in all_expressions_container. 
One stack frame takes O(n) space since it has various strings of length O(n). There are at most n nested recursive calls at any given time so maximum of O(n^2) space can be used for the stack.
In the worst case (think s="0000000000000", target=0) all 3^(n-1) generated expressions will evaluate to the target. That's O(n*3^n) space.
Total auxiliary space used would be O(n^2) + O(n*3^n) = O(n*3^n).
Space Complexity:
Also O(n*3^n).
'''
def generate_all_expressions(s, target):
    expressionCollection = []
    if not s:
        return expressionCollection

    def generate_all_expressions_dfs_helper(expressionSoFar, evaluatedValueSoFar, index, valueUpdateAtParentStep):
        if index == len(s):
            if evaluatedValueSoFar == target:
                expressionCollection.append(expressionSoFar)
            return

        for i in range(index, len(s)):
            # For any string this will check all possible subsets of the string for example for 
            # 12 it will check for 1, 2 and 12
            currentString = s[index:i+1]
            currentStringValue = int(currentString)
            if index == 0:
                generate_all_expressions_dfs_helper(expressionSoFar + currentString, currentStringValue, i+1, currentStringValue)
            else:
            # Reason for the following expression 
                # (evaluatedValueSoFar-valueUpdateAtParentStep) + (valueUpdateAtParentStep*currentStringValue) is:
                # For 123 the first time this code will get called will be when expressionSoFar is 1+2 evaluatedValueSoFar = 3 currentStringValue 3
                # the expressionSoFar + "*" + currentString = 1+2*3 as string which should evaluated to 1+(2*3) which is 7 and not (1+2)*3 which is 9 
                # In order to get 1 from 3 which is evaluatedValueSoFar we need to subtract the previousValue 2 from evaluated value which is 3
                # This expression arise from the InFix Tree for the expression and is dependent on the operators precedence.
                generate_all_expressions_dfs_helper(expressionSoFar + '*' + currentString, (evaluatedValueSoFar-valueUpdateAtParentStep) + (valueUpdateAtParentStep*currentStringValue), i+1, valueUpdateAtParentStep*currentStringValue)

                # For this expression the previous Value cannot be total Value so far it needs to be just the currentStringValue
                generate_all_expressions_dfs_helper(expressionSoFar + '+' + currentString, evaluatedValueSoFar+currentStringValue, i+1, currentStringValue)

    generate_all_expressions_dfs_helper('', 0, 0, 0)
    return expressionCollection

print(generate_all_expressions("123",6))
print(generate_all_expressions("2222",224))
print(generate_all_expressions("050505",5))
print(eval("1+2"))