def maxProductionProfit(numDays, productAProfit, productBProfit):
    if numDays == 0:
        return 0
    if numDays == 1:
        return max(productAProfit, productBProfit)
    if numDays == 2:
        return max(sum(productAProfit), sum(productBProfit))
    maxAProfit = [0, 0]
    maxBProfit = [0, 0]
    maxAProfit[0] = productAProfit[0]
    maxBProfit[0] = productBProfit[0]
    maxAProfit[1] = maxAProfit[0]+productAProfit[1]
    maxBProfit[1] = maxBProfit[0]+productBProfit[1]
    print(maxAProfit,maxBProfit)
    for idx in range(2,numDays):

        maxAProfit[(idx%2)], maxBProfit[(idx%2)] = max(maxAProfit[((idx-1)%2)] + productAProfit[idx],maxBProfit[((idx-2)%2)] + productAProfit[idx]), max(maxBProfit[((idx-1)%2)] + productBProfit[idx],maxAProfit[((idx-2)%2)] + productBProfit[idx])
    print(maxAProfit,maxBProfit)
    return max(maxAProfit[((numDays-1)%2)],maxBProfit[((numDays-1)%2)])

print(maxProductionProfit(4,[4,2,1,7],[1,2,5,4]))