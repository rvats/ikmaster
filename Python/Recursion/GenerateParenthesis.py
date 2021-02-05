def find_all_well_formed_brackets(n):
    parenthesisCollection = []
    str = [""] * 2 * n
    def find_all_well_formed_brackets_helper(str, pos, n, open, close, parenthesisCollection):
        if(close == n): 
            parenthesisCollection.append("".join(str))
        else: 
            if(open > close): 
                str[pos] = ')'
                find_all_well_formed_brackets_helper(str, pos + 1, n, open, close + 1, parenthesisCollection)
            if(open < n): 
                str[pos] = '('
                find_all_well_formed_brackets_helper(str, pos + 1, n, open + 1, close, parenthesisCollection)
    
    find_all_well_formed_brackets_helper(str, 0, n, 0, 0, parenthesisCollection)
    return(parenthesisCollection)
  
  
# Driver Code 
n = 3; 
for brackets in find_all_well_formed_brackets(n):
    print(brackets)