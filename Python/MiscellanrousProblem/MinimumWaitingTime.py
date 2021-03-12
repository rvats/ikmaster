def minimumWaitingTime(queries):
    queries.sort()
    waitTime = 0
    totalQueries=len(queries)
    for idx in range(1,totalQueries):
        waitTime+=((totalQueries-idx)*queries[idx-1])
    return waitTime
        

print(minimumWaitingTime([4,1,5]))
'''
1,4,5
1 - 0
4 - 1
5 - 4+1
'''
print(minimumWaitingTime([3,2,1,2,6]))
'''
1,2,2,3,6
1 - 0
2 - 1
2 - 2+1
3 - 2+2+1
6 - 3+2+2+1
'''