def maxGold(goldBagsCollection):
    gold = {}
    for idx in range(1, len(goldBagsCollection)+1):
        for left in range(0, len(goldBagsCollection)-idx+1):
            right = left + idx - 1
            if idx == 1:
                gold[(left,right)]=goldBagsCollection[left]
            elif idx == 2:
                gold[(left,right)]=max(goldBagsCollection[left],goldBagsCollection[right])
            else: 
                gold[(left,right)] = max
                (
                    goldBagsCollection[left] +
                    min(gold[(left+2,right)], gold[(left+1,right-1)]),
                    goldBagsCollection[right] + 
                    min(gold[(left+1,right)], gold[(left,right-1])))
    return gold[(0,len(goldBagsCollection))]

print(maxGold([6,10,5,2]))
print(maxGold([6,5,10,2]))