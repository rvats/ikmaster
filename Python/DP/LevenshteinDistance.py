'''
RECURRENCE RELATION:
for global input strings a, b:
def f(i, j):
    # base cases
    if j == 0:
        return i
    if i == 0:
        return j
    
    # recursive case
    if a[i-1] == b[j-1]:
        return f(i-1, j-1)
    else:
        add = 1 + f(i, j-1)
        del = 1 + f(i-1, j)
        rep = 1 + f(i-1, j-1)
        return min(add, del, rep)
'''

def  levenshteinDistance(strWord1, strWord2):
    # table to store subproblem results:
    rows = len(strWord1) + 1
    cols = len(strWord2) + 1
    table = [[None] * cols for _ in range(rows)]
    
    # fill basecases:
    for i in range(cols):
        table[0][i] = i # fill all columns of the first row
    for j in range(rows):
        table[j][0] = j # fill the first column in all rows
    
    # fill recursive cases:
    for j in range(1, rows):
        for i in range(1, cols):
            if strWord1[j-1] == strWord2[i-1]:
                table[j][i] = table[j-1][i-1]
            else:
                add = table[j-1][i]
                rem = table[j][i-1]
                rep = table[j-1][i-1]
                table[j][i] = 1 + min(add, rem, rep)
    
    return table[rows-1][cols-1]