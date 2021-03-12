'''
https://leetcode.com/problems/snakes-and-ladders/
909. Snakes and Ladders
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:
You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:
You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].
Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)
Return the least number of moves required to reach square N*N.  If it is not possible, return -1.
'''
class Solution(object):
    def snakesAndLadders(self, board):
        N = len(board)

        def getLocationOnBoard(s):
            # Given a square num s, return board coordinates (r, c)
            quot, rem = divmod(s-1, N)
            row = N - 1 - quot
            col = rem if row%2 != N%2 else N - 1 - rem
            return row, col

        dist = {1: 0}
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()
            if s == N*N: 
                return dist[s]
            for s2 in range(s+1, min(s+6, N*N) + 1):
                r, c = getLocationOnBoard(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    print(r, c)
                    print(board[r][c])
                    dist[s2] = dist[s] + 1
                    queue.append(s2)
        return -1