# Recursive Python function to solve tower of benaras
def towerOfBenaras(n , source, destination, auxilliary): 
    if n==1: 
        print("Move disk 1 from source ", source, " to destination ", destination)
        return
    towerOfBenaras(n-1, source, auxilliary, destination) 
    print("Move disk ", n," from source ", source, " to destination ", destination)
    towerOfBenaras(n-1, auxilliary, destination, source) 
          
# Driver code 
n = 6
towerOfBenaras(n,'A','B','C')