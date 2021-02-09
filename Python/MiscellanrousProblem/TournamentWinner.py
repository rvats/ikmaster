def tournamentWinner(competitions, results):
	leaderBoard = {}
	highestScore = 3
	for i in range(len(competitions)):
		winner = ""
		if results[i] == 0:
			winner = competitions[i][1]
		else:
			winner = competitions[i][0]
		if winner in leaderBoard:
			leaderBoard[winner]+=3
			highestScore+=3
		else:
			leaderBoard[winner]=3
	bestTeam = ""
	bestScore = 0
	for leader, score in leaderBoard.items():
		if score > bestScore:
			bestTeam = leader
			bestScore = score
	return bestTeam
		