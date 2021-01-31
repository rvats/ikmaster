# Naive Approach To Implement Combination
# Time Complexity = O(n^2) Space Complexity = O(1)
def combinationNaive(n,k):
  if k==0 or k==n:
     return 1
  elif n<k:
     return 0
  else:
     return combinationNaive(n-1, k-1) + combinationNaive(n-1, k)

N,K=11,6
for n in range(N):
    for k in range(K):
        print("C({},{})=".format(n,k),combinationNaive(n,k))


# Drawing Pascal Triangle
print("Pascal Triangle for n = 10")
# input n 
n = 11
for i in range(n): 
    for j in range(n-i+1): 
  
        # for left spacing 
        print(end=" ") 
  
    for j in range(i+1): 
  
        # nCr = n!/((n-r)!*r!) 
        print(combinationNaive(i,j), end=" ") 
  
    # for new line 
    print() 