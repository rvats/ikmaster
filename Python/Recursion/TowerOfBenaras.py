# Recursive Python function to solve tower of benaras
numberOfMoves = 0
def towerOfBenaras(n , source, destination, auxilliary): 
    global numberOfMoves
    if n==1: 
        numberOfMoves+=1
        print("Move disk 1 from source ", source, " to destination ", destination, "Moves Count: ", numberOfMoves)
        return
    towerOfBenaras(n-1, source, auxilliary, destination) 
    numberOfMoves+=1
    print("Move disk ", n," from source ", source, " to destination ", destination, "Moves Count: ", numberOfMoves)
    towerOfBenaras(n-1, auxilliary, destination, source) 
          
# Driver code 
n = 3
towerOfBenaras(n,'A','B','C')