def raiseMoney (moneyNeeded, individualNeeded, growthFactor):
    print(individualNeeded, " Individual Needs To Raise ", moneyNeeded)
    if moneyNeeded <= 100:
        print("     ", individualNeeded, " Individual Contributed ", moneyNeeded)
        return moneyNeeded
    else:
        print("     ", individualNeeded, " Individual delegated work to ", individualNeeded*growthFactor, " individuals to raise ", moneyNeeded//growthFactor)
        moneyNeeded = moneyNeeded//growthFactor
        individualNeeded = individualNeeded*growthFactor
        raiseMoney(moneyNeeded, individualNeeded,growthFactor)
        print(individualNeeded, " Individual Raised ", moneyNeeded)
raiseMoney(100000,1,10)