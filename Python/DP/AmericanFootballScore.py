'''
How many ways to get the final score in an American Football Game
''',
def waysToFinalScoreNaiveRecursion(finalScore):
    if finalScore == 0 or finalScore == 2 or finalScore == 3:
        return 1
    elif finalScore == 1:
        return 0
    elif finalScore == 6: 
        return 3

    return waysToFinalScoreNaiveRecursion(finalScore-2) + waysToFinalScoreNaiveRecursion(finalScore-3) + waysToFinalScoreNaiveRecursion(finfinalScore)

def waysToFinalScoreONSpace(finalScore):
    if finalScore < 0:
        return 0
    scoreArray = [0] * (finalScore+1)
    scoreArray[0] = 1
    for score in range(2,finalScore+1):
        score2 = scoreArray[score-2]if score >= 2 else 0
        score3 = scoreArray[score-3] if score >= 3  else 0
        score6 = scoreArray[score-6] if score >= 6 else 0
        scoreArray[score] = score2 + score3 + score6
    print(finalScore, scoreArray)
    return scoreArray[finalScore]

def waysToFinalScore(finalScore):
    if finalScore < 0:
        return 0
    scoreArray = [0] * 6
    scoreArray[0] = 1
    for score in range(2,finalScore+1):
        scoreArray[(score-2)%6] = scoreArray[(score-2)%6] if score >= 2 else 0
        scoreArray[(score-3)%6] = scoreArray[(score-3)%6] if score >= 3  else 0
        scoreArray[(score-6)%6] = scoreArray[(score-6)%6] if score >= 6 else 0
        scoreArray[score%6] = scoreArray[(score-2)%6] + scoreArray[(score-3)%6] + scoreArray[(score-6)%6]
    print(finalScore, scoreArray)
    return scoreArray[finalScore%6]

for score in range(101):
    print(score, waysToFinalScore(score))