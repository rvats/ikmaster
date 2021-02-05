def find_all_arrangements(n):
    candidate = [None] * n
    solutions = []
    col_occupied = [False] * n
    slash_diagonal_occupied = [False] * (2*n-1)
    backslash_diagonal_occupied = [False] * (2*n-1)

    def is_safe(row, col):
        return not (col_occupied[col] or
                    slash_diagonal_occupied[row+col] or
                    backslash_diagonal_occupied[row-col+n-1])

    def generate_output(solutions):
        output = []
        for arr in solutions:
            o = [['-'] * len(arr) for _ in range(len(arr))]
            for r, c in enumerate(arr):
                o[r][c] = 'q'
            output.append([''.join(row) for row in o])
        return output

    def find_all_arrangements_util(candidate, row):
        if row == n:
            solutions.append([x for x in candidate])
            return
        for col in range(0, n):
            if is_safe(row, col):
                candidate[row] = col
                col_occupied[col] = True
                slash_diagonal_occupied[row+col] = True
                backslash_diagonal_occupied[row-col+n-1] = True
                find_all_arrangements_util(candidate, row+1)
                col_occupied[col] = False
                slash_diagonal_occupied[row+col] = False
                backslash_diagonal_occupied[row-col+n-1] = False

    find_all_arrangements_util(candidate, 0)
    return generate_output(solutions)

# driver program to test above function 
for number in range(2,9):
    print(find_all_arrangements(number))
    print("===============================================================")