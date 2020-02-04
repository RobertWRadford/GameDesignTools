def main():
	theMap = [[8, 8, 8, 8, 8, 8, 8],
			[8, 8, 8, 8, 8, 8, 8],
			[8, 8, 8, 8, 8, 8, 8],
			[8, 8, 8, 8, 8, 8, 8],
			[8, 8, 8, 8, 8, 8, 8],
			[8, 8, 8, 8, 8, 8, 8],
			[8, 8, 8, 8, 8, 8, 8],
			[8, 8, 8, 8, 8, 8, 8],
			[8, 8, 8, 8, 8, 8, 8]]

	print("\n\n"+str(theMap[0][0])+str(theMap[0][1])+str(theMap[0][2])+str(theMap[0][3])+str(theMap[0][4])+str(theMap[0][5])+str(theMap[0][6])+"\n"+str(theMap[1][0])+str(theMap[1][1])+str(theMap[1][2])+str(theMap[1][3])+str(theMap[1][4])+str(theMap[1][5])+str(theMap[1][6])+"\n"+str(theMap[2][0])+str(theMap[2][1])+str(theMap[2][2])+str(theMap[2][3])+str(theMap[2][4])+str(theMap[2][5])+str(theMap[2][6])+"\n"+str(theMap[3][0])+str(theMap[3][1])+str(theMap[3][2])+str(theMap[3][3])+str(theMap[3][4])+str(theMap[3][5])+str(theMap[3][6])+"\n"+str(theMap[4][0])+str(theMap[4][1])+str(theMap[4][2])+str(theMap[4][3])+str(theMap[4][4])+str(theMap[4][5])+str(theMap[4][6])+"\n"+str(theMap[5][0])+str(theMap[5][1])+str(theMap[5][2])+str(theMap[5][3])+str(theMap[5][4])+str(theMap[5][5])+str(theMap[5][6])+"\n"+str(theMap[6][0])+str(theMap[6][1])+str(theMap[6][2])+str(theMap[6][3])+str(theMap[6][4])+str(theMap[6][5])+str(theMap[6][6])+"\n"+str(theMap[7][0])+str(theMap[7][1])+str(theMap[7][2])+str(theMap[7][3])+str(theMap[7][4])+str(theMap[7][5])+str(theMap[7][6])+"\n"+str(theMap[8][0])+str(theMap[8][1])+str(theMap[8][2])+str(theMap[8][3])+str(theMap[8][4])+str(theMap[8][5])+str(theMap[8][6])+"\n")
	
	n = 0
	while n < 9:
		k = 0
		while k < 7:
			try:
				path = input("\ninput a 1 or a 0.\n")
				path = int(path)
				if path != 1 and path != 0:
					print("\nPlease input only a 1 or a 0.")
				else:
					theMap[n][k] = path
					print("\n\n"+str(theMap[0][0])+str(theMap[0][1])+str(theMap[0][2])+str(theMap[0][3])+str(theMap[0][4])+str(theMap[0][5])+str(theMap[0][6])+"\n"+str(theMap[1][0])+str(theMap[1][1])+str(theMap[1][2])+str(theMap[1][3])+str(theMap[1][4])+str(theMap[1][5])+str(theMap[1][6])+"\n"+str(theMap[2][0])+str(theMap[2][1])+str(theMap[2][2])+str(theMap[2][3])+str(theMap[2][4])+str(theMap[2][5])+str(theMap[2][6])+"\n"+str(theMap[3][0])+str(theMap[3][1])+str(theMap[3][2])+str(theMap[3][3])+str(theMap[3][4])+str(theMap[3][5])+str(theMap[3][6])+"\n"+str(theMap[4][0])+str(theMap[4][1])+str(theMap[4][2])+str(theMap[4][3])+str(theMap[4][4])+str(theMap[4][5])+str(theMap[4][6])+"\n"+str(theMap[5][0])+str(theMap[5][1])+str(theMap[5][2])+str(theMap[5][3])+str(theMap[5][4])+str(theMap[5][5])+str(theMap[5][6])+"\n"+str(theMap[6][0])+str(theMap[6][1])+str(theMap[6][2])+str(theMap[6][3])+str(theMap[6][4])+str(theMap[6][5])+str(theMap[6][6])+"\n"+str(theMap[7][0])+str(theMap[7][1])+str(theMap[7][2])+str(theMap[7][3])+str(theMap[7][4])+str(theMap[7][5])+str(theMap[7][6])+"\n"+str(theMap[8][0])+str(theMap[8][1])+str(theMap[8][2])+str(theMap[8][3])+str(theMap[8][4])+str(theMap[8][5])+str(theMap[8][6])+"\n")
					k+=1
			except:
				print("\nPlease input only a 1 or 0.")
		n+=1

	shownMap = {
	"0-0": "■",
	"0-1": "■",
	"0-2": "■",
	"0-3": "■",
	"0-4": "■",
	"0-5": "■",
	"0-6": "■",
	"1-0": "■",
	"1-1": "■",
	"1-2": "■",
	"1-3": "■",
	"1-4": "■",
	"1-5": "■",
	"1-6": "■",
	"2-0": "■",
	"2-1": "■",
	"2-2": "■",
	"2-3": "■",
	"2-4": "■",
	"2-5": "■",
	"2-6": "■",
	"3-0": "■",
	"3-1": "■",
	"3-2": "■",
	"3-3": "■",
	"3-4": "■",
	"3-5": "■",
	"3-6": "■",
	"4-0": "■",
	"4-1": "■",
	"4-2": "■",
	"4-3": "■",
	"4-4": "■",
	"4-5": "■",
	"4-6": "■",
	"5-0": "■",
	"5-1": "■",
	"5-2": "■",
	"5-3": "■",
	"5-4": "■",
	"5-5": "■",
	"5-6": "■",
	"6-0": "■",
	"6-1": "■",
	"6-2": "■",
	"6-3": "■",
	"6-4": "■",
	"6-5": "■",
	"6-6": "■",
	"7-0": "■",
	"7-1": "■",
	"7-2": "■",
	"7-3": "■",
	"7-4": "■",
	"7-5": "■",
	"7-6": "■",
	"8-0": "■",
	"8-1": "■",
	"8-2": "■",
	"8-3": "■",
	"8-4": "■",
	"8-5": "■",
	"8-6": "■",
	}

	posRow = 7
	posCol = 1
	j = 0
	while j < 9:
		i = 0
		while i < 7:
			if theMap[j][i] == 0:
				shownMap[str(j)+"-"+str(i)] = "■"
				i+=1
			else:
				shownMap[str(j)+"-"+str(i)] = "░"
				i+=1
		j+=1

	shownMap[str(posRow)+"-"+str(posCol)] = "X"

	while posRow != 0 or posCol != 2:
		print("\n\n"+shownMap["0-0"]+shownMap["0-1"]+shownMap["0-2"]+shownMap["0-3"]+shownMap["0-4"]+shownMap["0-5"]+shownMap["0-6"]+"\n"+shownMap["1-0"]+shownMap["1-1"]+shownMap["1-2"]+shownMap["1-3"]+shownMap["1-4"]+shownMap["1-5"]+shownMap["1-6"]+"\n"+shownMap["2-0"]+shownMap["2-1"]+shownMap["2-2"]+shownMap["2-3"]+shownMap["2-4"]+shownMap["2-5"]+shownMap["2-6"]+"\n"+shownMap["3-0"]+shownMap["3-1"]+shownMap["3-2"]+shownMap["3-3"]+shownMap["3-4"]+shownMap["3-5"]+shownMap["3-6"]+"\n"+shownMap["4-0"]+shownMap["4-1"]+shownMap["4-2"]+shownMap["4-3"]+shownMap["4-4"]+shownMap["4-5"]+shownMap["4-6"]+"\n"+shownMap["5-0"]+shownMap["5-1"]+shownMap["5-2"]+shownMap["5-3"]+shownMap["5-4"]+shownMap["5-5"]+shownMap["5-6"]+"\n"+shownMap["6-0"]+shownMap["6-1"]+shownMap["6-2"]+shownMap["6-3"]+shownMap["6-4"]+shownMap["6-5"]+shownMap["6-6"]+"\n"+shownMap["7-0"]+shownMap["7-1"]+shownMap["7-2"]+shownMap["7-3"]+shownMap["7-4"]+shownMap["7-5"]+shownMap["7-6"]+"\n"+shownMap["8-0"]+shownMap["8-1"]+shownMap["8-2"]+shownMap["8-3"]+shownMap["8-4"]+shownMap["8-5"]+shownMap["8-6"]+"\n\n")
		move = input("\n\n move up, down, right, or left?\n\n")
		if move == "down":
			if posRow == 8 or theMap[posRow+1][posCol] == 0:
				print("\nCannot move down")
			else:
				shownMap[str(posRow)+"-"+str(posCol)] = "░"
				posRow+=1
				shownMap[str(posRow)+"-"+str(posCol)] = "X"					
		elif move == "up":
			if posRow == 0 or theMap[posRow-1][posCol] == 0:
				print("\nCannot move up")
			else:
				shownMap[str(posRow)+"-"+str(posCol)] = "░"
				posRow-=1
				shownMap[str(posRow)+"-"+str(posCol)] = "X"
		elif move == "right":
			if posCol == 6 or theMap[posRow][posCol+1] == 0:
				print("\nCannot move right.")
			else:
				shownMap[str(posRow)+"-"+str(posCol)] = "░"
				posCol+=1
				shownMap[str(posRow)+"-"+str(posCol)] = "X"
		elif move == "left":
			if posCol == 0 or theMap[posRow][posCol-1] == 0:
				print("\nCannot move left")
			else:
				shownMap[str(posRow)+"-"+str(posCol)] = "░"
				posCol-=1
				shownMap[str(posRow)+"-"+str(posCol)] = "X"
	print("\n\nYou did it!!")
	
main()
