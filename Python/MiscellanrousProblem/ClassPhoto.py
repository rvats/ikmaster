def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()
	blueShirtHeights.sort()
	if len(redShirtHeights)==1:
		return redShirtHeights[0] != blueShirtHeights[0]
	redShirtsInFront = redShirtHeights[0] < blueShirtHeights[0]
	for i in range(1,len(redShirtHeights)):
		if (redShirtsInFront and redShirtHeights[i] > blueShirtHeights[i]) 	or ( not redShirtsInFront and redShirtHeights[i] < blueShirtHeights[i]) or (redShirtHeights[i] == blueShirtHeights[i]):
			return False
	return True