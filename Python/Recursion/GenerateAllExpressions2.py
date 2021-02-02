# Complete the function below.
def generate_all_expressions(s, target):
    expressionCollection = []
    if not s:
        return expressionCollection
    def generate_all_expressions_helper(s, target, index, slate, currentValue, previousValue, expressionCollection):
        if index == len(s):
            if currentValue == target:
                expressionCollection.append(slate)
        else:
            for i in range(index, len(s)):
                currentExpression = s[index:i+1] 
                # index = 0 (2,222), (22,22), (222,2) (2222) 
                # index = 1 2(2,22), 2(22,2), 2(222)
                currentExpressionValue = int(currentExpression)
                if currentValue<=target:
                    if index == 0: # or len(slate) == 0
                        generate_all_expressions_helper(s, target, index+1, slate+currentExpression, currentExpressionValue, currentExpressionValue, expressionCollection)
                    else:
                        generate_all_expressions_helper(s, target, index+1, slate+"*"+s[index], (currentValue+currentExpressionValue), (previousValue*currentExpressionValue), expressionCollection)
                        generate_all_expressions_helper(s, target, index+1, slate+"+"+s[index], currentValue+currentExpressionValue, currentExpressionValue, expressionCollection)
    generate_all_expressions_helper(s, target, 0, "", 0, 0, expressionCollection)
    return expressionCollection



print(generate_all_expressions("123", 6))
#print(generate_all_expressions("2222", 224)) 
''''
2*2*2*2
2*2+2*2
# * take precedence
                        # 2+2*2 = 6 // 8
                        #generate_all_expressions_helper(s, target, index+1, slate+"*"+s[index], (currentValue-previousValue) + (previousValue*currentExpressionValue), (previousValue*currentExpressionValue), expressionCollection)
'''
