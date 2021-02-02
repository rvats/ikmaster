def generate_all_expressions(s, target):
    if not s:
        return []
    output = []
    def _helper(currentExpression, evaluated, idx, prev):
        if idx == len(s):
            if evaluated == target:
                output.append(currentExpression)
            return
        for i in range(idx, len(s)):
            curr = s[idx:i+1]
            curr_int = int(curr)
            if idx == 0:
                _helper(currentExpression + curr, curr_int, i+1, curr_int)
            else:
                _helper(currentExpression + '+' + curr, evaluated+curr_int, i+1, curr_int)
                _helper(currentExpression + '*' + curr, (evaluated-prev) + (prev*curr_int), i+1, prev*curr_int)

    _helper('', 0, 0, 0)
    return output

print(generate_all_expressions("123", 6))
print(generate_all_expressions("222", 24))