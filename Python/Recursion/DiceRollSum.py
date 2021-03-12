# BackTrack Problem - Dice Roll Sum
def diceRollSum(numberOfDices, targetSum, facesOnDice):
      mod = 1000000000+7
      dp =[[0 for i in range(targetSum+1)] for j in range(numberOfDices)]
      for i in range(numberOfDices):
         for j in range(targetSum+1):
            if i == 0:
               dp[i][j] = 1 if j>=1 and j<=facesOnDice else 0
            else:
               for l in range(1,facesOnDice+1):
                  if j-l>0:
                     dp[i][j]+=dp[i-1][j-l]
                     dp[i][j]%=mod
      return dp [numberOfDices-1][targetSum] % mod
print(diceRollSum(2,7,6)) #  5

def diceRollSumDriver(numberOfDices, targetSum, facesOnDice):
    diceRollSumHelper(numberOfDices, targetSum, facesOnDice, 0, [])

def diceRollSumHelper(numberOfDices, targetSum, facesOnDice, currentSum, soFar):
    if currentSum > targetSum and numberOfDices < 0:
        return
    if numberOfDices == 0 and currentSum == targetSum:
        print(soFar)
    else:
        for faceValue in range(1,facesOnDice+1):
            soFar.append(faceValue)
            diceRollSumHelper(numberOfDices-1,targetSum,facesOnDice,currentSum+faceValue,soFar)
            soFar.pop()
diceRollSumDriver(2,7,6)

'''
1,6
2,5
3,4
4,3
5,2
6,1
'''