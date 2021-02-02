def generate_all_expressions(s, target):
    expressionCollection = []
    if not s:
        return expressionCollection

    def generate_all_expressions_dfs_helper(expressionSoFar, index):
        if index == len(s):
            if eval(expressionSoFar) == target:
                expressionCollection.append(expressionSoFar)
            return

        for i in range(index, len(s)):
            currentString = s[index:i+1]
            if index == 0:
                generate_all_expressions_dfs_helper(expressionSoFar + currentString, i+1)
            else:
                generate_all_expressions_dfs_helper(expressionSoFar + '*' + currentString, i+1)
                generate_all_expressions_dfs_helper(expressionSoFar + '+' + currentString, i+1,)

    generate_all_expressions_dfs_helper('', 0)
    return expressionCollection

print(generate_all_expressions("123",6))
print(generate_all_expressions("2222",224))
# print(generate_all_expressions("050505",5))
# print(eval("0+5+0*5*05"))
