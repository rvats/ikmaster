def numberOfWaysToTraverseGraph(width, height):
	grid = [[1] * width for h in range(height)]
	for h in range(height):
		grid[h][0]=1
	for h in range(1, height):
		for w in range(1, width):
			grid[h][w]=grid[h-1][w]+grid[h][w-1]
	return grid[-1][-1]
