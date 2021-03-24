import random
def shuffle(deck):
	for i in range(len(deck)):
		x = random.randint(i,len(deck)-1)
		deck[i],deck[x] = deck[x], deck[i]
	return deck
deck = [i for i in range(52)]
print(shuffle(deck))
print(shuffle(deck))
deck1 = [4, 17, 35, 46, 39, 22, 31, 40, 36, 6, 49, 16, 47, 44, 32, 23, 8, 14, 5, 33, 9, 38, 29, 43, 24, 30, 50, 10, 25, 28, 12, 0, 1, 21, 51, 37, 26, 15, 7, 3, 41, 19, 2, 48, 45, 42, 27, 11, 20, 13, 34, 18]
deck1.sort()
print(deck1)
deck2 = [24, 40, 50, 25, 43, 10, 48, 46, 7, 18, 21, 17, 31, 4, 9, 0, 14, 32, 16, 29, 19, 37, 5, 15, 39, 13, 23, 49, 3, 8, 34, 28, 20, 47, 26, 45, 11, 44, 51, 6, 2, 41, 30, 22, 12, 36, 1, 38, 27, 33, 42, 35]
deck2.sort()
print(deck2)