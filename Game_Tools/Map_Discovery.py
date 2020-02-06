
#Map discovery
def printEnvironment(Map, showMap, curY, curX, lastRow, lastCol):
	
	showMap[str(curY)+"-"+str(curX)] = "X"
	
	if curX != 1:
		if curX != 2:
			if Map[curY][curX-1] == 0:
				showMap[str(curY)+"-"+str(curX-1)] = "█"
			elif Map[curY][curX-1] == 1:
				showMap[str(curY)+"-"+str(curX-1)] = "░"
			else:
				showMap[str(curY)+"-"+str(curX-1)] = "▓"

			if Map[curY][curX-1] != 0 and Map[curY][curX-2] == 0:
				showMap[str(curY)+"-"+str(curX-2)] = "█"
			elif Map[curY][curX-1] != 0 and Map[curY][curX-2] == 1:
				showMap[str(curY)+"-"+str(curX-2)] = "░"
			elif Map[curY][curX-1] != 0 and Map[curY][curX-2] != (0 or 1):
				showMap[str(curY)+"-"+str(curX-2)] = "▓"
		else:
			if Map[curY][curX-1] == 0:
				showMap[str(curY)+"-"+str(curX-1)] = "█"
			elif Map[curY][curX-1] == 1:
				showMap[str(curY)+"-"+str(curX-1)] = "░"
			else:
				showMap[str(curY-1)+"-"+str(curX-1)] = "▓"
	
	if curX != lastCol-1:
		if curX != lastCol-2:
			if Map[curY][curX+1] == 0:
				showMap[str(curY)+"-"+str(curX+1)] = "█"
			elif Map[curY][curX+1] == 1:
				showMap[str(curY)+"-"+str(curX+1)] = "░"
			else:
				showMap[str(curY)+"-"+str(curX+1)] = "▓"

			if Map[curY][curX+1] != 0 and Map[curY][curX+2] == 0:
				showMap[str(curY)+"-"+str(curX+2)] = "█"
			elif Map[curY][curX+1] != 0 and Map[curY][curX+2] == 1:
				showMap[str(curY)+"-"+str(curX+2)] = "░"
			elif Map[curY][curX+1] != 0 and Map[curY][curX+2] != (0 or 1):
				showMap[str(curY)+"-"+str(curX+2)] = "▓"
		else:
			if Map[curY][curX+1] == 0:
				showMap[str(curY)+"-"+str(curX+1)] = "█"
			elif Map[curY][curX+1] == 1:
				showMap[str(curY)+"-"+str(curX+1)] = "░"
			else:
				showMap[str(curY)+"-"+str(curX+1)] = "▓"
	
	if curY != lastRow-1:
		if curY != lastRow-2:
			if Map[curY+1][curX] == 0:
				showMap[str(curY+1)+"-"+str(curX)] = "█"
			elif Map[curY+1][curX] == 1:
				showMap[str(curY+1)+"-"+str(curX)] = "░"
			else:
				showMap[str(curY+1)+"-"+str(curX)] = "▓"

			if Map[curY+1][curX] != 0 and Map[curY+2][curX] == 0:
				showMap[str(curY+2)+"-"+str(curX)] = "█"
			elif Map[curY+1][curX] != 0 and Map[curY+2][curX] == 1:
				showMap[str(curY+2)+"-"+str(curX)] = "░"
			elif Map[curY+1][curX] != 0 and Map[curY+2][curX] != (0 or 1):
				showMap[str(curY+2)+"-"+str(curX)] = "▓"
		else:
			if Map[curY+1][curX] == 0:
				showMap[str(curY+1)+"-"+str(curX)] = "█"
			elif Map[curY+1][curX] == 1:
				showMap[str(curY+1)+"-"+str(curX)] = "░"
			else:
				showMap[str(curY+1)+"-"+str(curX)] = "▓"

	if curY != 1:
		if curY != 2:
			if Map[curY-1][curX] == 0:
				showMap[str(curY-1)+"-"+str(curX)] = "█"
			elif Map[curY-1][curX] == 1:
				showMap[str(curY-1)+"-"+str(curX)] = "░"
			else:
				showMap[str(curY-1)+"-"+str(curX)] = "▓"

			if Map[curY-1][curX] != 0 and Map[curY-2][curX] == 0:
				showMap[str(curY-2)+"-"+str(curX)] = "█"
			elif Map[curY-1][curX] != 0 and Map[curY-2][curX] == 1:
				showMap[str(curY-2)+"-"+str(curX)] = "░"
			elif Map[curY-1][curX] != 0 and Map[curY-2][curX] != (0 or 1):
				showMap[str(curY-2)+"-"+str(curX)] = "▓"
		else:
			if Map[curY-1][curX] == 0:
				showMap[str(curY-1)+"-"+str(curX)] = "█"
			elif Map[curY-1][curX] == 1:
				showMap[str(curY-1)+"-"+str(curX)] = "░"
			else:
				showMap[str(curY-1)+"-"+str(curX)] = "▓"
	
	if curX != 1 and curY != 1:
		if Map[curY-1][curX] != 0 or Map[curY][curX-1] != 0:
			if Map[curY-1][curX-1] == 0:
				showMap[str(curY-1)+"-"+str(curX-1)] = "█"
			elif Map[curY-1][curX-1] == 1:
				showMap[str(curY-1)+"-"+str(curX-1)] = "░"
			else:
				showMap[str(curY-1)+"-"+str(curX-1)] = "▓"
	
	
	if curX != lastCol-1 and curY != 1:
		if Map[curY-1][curX] != 0 or Map[curY][curX+1] != 0:
			if Map[curY-1][curX+1] == 0:
				showMap[str(curY-1)+"-"+str(curX+1)] = "█"
			elif Map[curY-1][curX+1] == 1:
				showMap[str(curY-1)+"-"+str(curX+1)] = "░"
			else:
				showMap[str(curY-1)+"-"+str(curX+1)] = "▓"
	
	
	if curX != lastCol-1 and curY != lastRow-1:
		if Map[curY+1][curX] != 0 or Map[curY][curX+1] != 0:
			if Map[curY+1][curX+1] == 0:
				showMap[str(curY+1)+"-"+str(curX+1)] = "█"
			elif Map[curY+1][curX+1] == 1:
				showMap[str(curY+1)+"-"+str(curX+1)] = "░"
			else:
				showMap[str(curY+1)+"-"+str(curX+1)] = "▓"
	

	if curX != 1 and curY != lastRow-1:
		if Map[curY+1][curX] != 0 or Map[curY][curX-1] != 0:
			if Map[curY+1][curX-1] == 0:
				showMap[str(curY+1)+"-"+str(curX-1)] = "█"
			elif Map[curY+1][curX-1] == 1:
				showMap[str(curY+1)+"-"+str(curX-1)] = "░"
			else:
				showMap[str(curY+1)+"-"+str(curX-1)] = "▓"
	
	return(showMap)


def main():
	#Map information
	map1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 1, 0, 0, 0, 0],
		    [0, 0, 0, 1, 1, 1, 0, 0, 0],
		    [0, 0, 1, 1, 1, 1, 5, 0, 0],
		    [0, 0, 0, 1, 3, 1, 0, 0, 0],
		    [0, 0, 0, 0, 1, 0, 0, 0, 0],
		    [0, 0, 0, 0, 4, 0, 0, 0, 0],
		    [0, 0, 0, 0, 1, 0, 0, 0, 0],
		    [0, 0, 0, 0, 1, 0, 0, 0, 0],
		    [0, 0, 0, 0, 2, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

	shownMap = {
	"0-0": "╔",
	"0-1": "═",
	"0-2": "═",
	"0-3": "═",
	"0-4": "═",
	"0-5": "═",
	"0-6": "═",
	"0-7": "═",
	"0-8": "╗",
	"1-0": "║",
	"1-1": " ",
	"1-2": " ",
	"1-3": " ",
	"1-4": " ",
	"1-5": " ",
	"1-6": " ",
	"1-7": " ",
	"1-8": "║",
	"2-0": "║",
	"2-1": " ",
	"2-2": " ",
	"2-3": " ",
	"2-4": " ",
	"2-5": " ",
	"2-6": " ",
	"2-7": " ",
	"2-8": "║",
	"3-0": "║",
	"3-1": " ",
	"3-2": " ",
	"3-3": " ",
	"3-4": " ",
	"3-5": " ",
	"3-6": " ",
	"3-7": " ",
	"3-8": "║",
	"4-0": "║",
	"4-1": " ",
	"4-2": " ",
	"4-3": " ",
	"4-4": " ",
	"4-5": " ",
	"4-6": " ",
	"4-7": " ",
	"4-8": "║",
	"5-0": "║",
	"5-1": " ",
	"5-2": " ",
	"5-3": " ",
	"5-4": " ",
	"5-5": " ",
	"5-6": " ",
	"5-7": " ",
	"5-8": "║",
	"6-0": "║",
	"6-1": " ",
	"6-2": " ",
	"6-3": " ",
	"6-4": " ",
	"6-5": " ",
	"6-6": " ",
	"6-7": " ",
	"6-8": "║",
	"7-0": "║",
	"7-1": " ",
	"7-2": " ",
	"7-3": " ",
	"7-4": " ",
	"7-5": " ",
	"7-6": " ",
	"7-7": " ",
	"7-8": "║",
	"8-0": "║",
	"8-1": " ",
	"8-2": " ",
	"8-3": " ",
	"8-4": " ",
	"8-5": " ",
	"8-6": " ",
	"8-7": " ",
	"8-8": "║",
	"9-0": "║",
	"9-1": " ",
	"9-2": " ",
	"9-3": " ",
	"9-4": " ",
	"9-5": " ",
	"9-6": " ",
	"9-7": " ",
	"9-8": "║",
	"10-0": "╚",
	"10-1": "═",
	"10-2": "═",
	"10-3": "═",
	"10-4": "═",
	"10-5": "═",
	"10-6": "═",
	"10-7": "═",
	"10-8": "╝",
	}

	curY = 7
	curX = 4
	curPos = map1[curY][curX]
	lastRow = 10
	lastCol = 8


	while curY != 1 or curX != 4:
		shownMap = printEnvironment(map1, shownMap, curY, curX, lastRow, lastCol)
		print("\n\n"+shownMap["0-0"]+shownMap["0-1"]+shownMap["0-2"]+shownMap["0-3"]+shownMap["0-4"]+shownMap["0-5"]+shownMap["0-6"]+shownMap["0-7"]+shownMap["0-8"]+"\n"+shownMap["1-0"]+shownMap["1-1"]+shownMap["1-2"]+shownMap["1-3"]+shownMap["1-4"]+shownMap["1-5"]+shownMap["1-6"]+shownMap["1-7"]+shownMap["1-8"]+"\n"+shownMap["2-0"]+shownMap["2-1"]+shownMap["2-2"]+shownMap["2-3"]+shownMap["2-4"]+shownMap["2-5"]+shownMap["2-6"]+shownMap["2-7"]+shownMap["2-8"]+"\n"+shownMap["3-0"]+shownMap["3-1"]+shownMap["3-2"]+shownMap["3-3"]+shownMap["3-4"]+shownMap["3-5"]+shownMap["3-6"]+shownMap["3-7"]+shownMap["3-8"]+"\n"+shownMap["4-0"]+shownMap["4-1"]+shownMap["4-2"]+shownMap["4-3"]+shownMap["4-4"]+shownMap["4-5"]+shownMap["4-6"]+shownMap["4-7"]+shownMap["4-8"]+"\n"+shownMap["5-0"]+shownMap["5-1"]+shownMap["5-2"]+shownMap["5-3"]+shownMap["5-4"]+shownMap["5-5"]+shownMap["5-6"]+shownMap["5-7"]+shownMap["5-8"]+"\n"+shownMap["6-0"]+shownMap["6-1"]+shownMap["6-2"]+shownMap["6-3"]+shownMap["6-4"]+shownMap["6-5"]+shownMap["6-6"]+shownMap["6-7"]+shownMap["6-8"]+"\n"+shownMap["7-0"]+shownMap["7-1"]+shownMap["7-2"]+shownMap["7-3"]+shownMap["7-4"]+shownMap["7-5"]+shownMap["7-6"]+shownMap["7-7"]+shownMap["7-8"]+"\n"+shownMap["8-0"]+shownMap["8-1"]+shownMap["8-2"]+shownMap["8-3"]+shownMap["8-4"]+shownMap["8-5"]+shownMap["8-6"]+shownMap["8-7"]+shownMap["8-8"]+"\n"+shownMap["9-0"]+shownMap["9-1"]+shownMap["9-2"]+shownMap["9-3"]+shownMap["9-4"]+shownMap["9-5"]+shownMap["9-6"]+shownMap["9-7"]+shownMap["9-8"]+"\n"+shownMap["10-0"]+shownMap["10-1"]+shownMap["10-2"]+shownMap["10-3"]+shownMap["10-4"]+shownMap["10-5"]+shownMap["10-6"]+shownMap["10-7"]+shownMap["10-8"]+"\n\n")
		move = input("move up, down, right, or left?\n\n8.) Up\n6.) Right\n4.) Left\n2.) Down\n\n")
	
		#Moving Down
		
		if move == "2":
			if curY == lastRow-1 or map1[curY+1][curX] == 0:
				print("\nCannot move down\n")

			elif map1[curY+1][curX] == 1:
				curY+=1

			elif map1[curY+1][curX] == 2:
				curY+=1
				print("\nDead end!\n")

			elif map1[curY+1][curX] == 3:
				curY+=1
				print("\nYou're leaving the clearing.\n")
		
			elif map1[curY+1][curX] == 4:
				curY+=1
				print("\nThe rats are still there and still friendly!\n")
		
		#Moving Up

		elif move == "8":
			
			if curY == 1 or map1[curY-1][curX] == 0:
				print("\nCannot move up")
			
			elif map1[curY-1][curX] == 1:
				curY-=1 
			
			elif map1[curY-1][curX] == 3:
				curY-=1
				print("\nYou walk into a large clearing.\n")
			
			elif map1[curY-1][curX] == 4:
				curY-=1
				print("\nYou meet some friendly rats.\n")


		#Moving Right

		elif move == "6":
			
			if curX == lastCol-1 or map1[curY][curX+1] == 0:
				print("\nCannot move right.")
			
			elif map1[curY][curX+1] == 1:
				curX+=1
			
			elif map1[curY][curX+1] == 5:
				curX+=1
				print("This waters gross..")
		

		#Moving Left

		elif move == "4":
			
			if curX == 1 or map1[curY][curX-1] == 0:
				print("\nCannot move left")
			
			else:
				curX-=1
		

		#Correcting

		else:
			print("Please input '8' '6' '4' or '2'")
	


	shownMap = printEnvironment(map1, shownMap, curY, curX, lastRow, lastCol)
	print("\n\n"+shownMap["0-0"]+shownMap["0-1"]+shownMap["0-2"]+shownMap["0-3"]+shownMap["0-4"]+shownMap["0-5"]+shownMap["0-6"]+shownMap["0-7"]+shownMap["0-8"]+"\n"+shownMap["1-0"]+shownMap["1-1"]+shownMap["1-2"]+shownMap["1-3"]+shownMap["1-4"]+shownMap["1-5"]+shownMap["1-6"]+shownMap["1-7"]+shownMap["1-8"]+"\n"+shownMap["2-0"]+shownMap["2-1"]+shownMap["2-2"]+shownMap["2-3"]+shownMap["2-4"]+shownMap["2-5"]+shownMap["2-6"]+shownMap["2-7"]+shownMap["2-8"]+"\n"+shownMap["3-0"]+shownMap["3-1"]+shownMap["3-2"]+shownMap["3-3"]+shownMap["3-4"]+shownMap["3-5"]+shownMap["3-6"]+shownMap["3-7"]+shownMap["3-8"]+"\n"+shownMap["4-0"]+shownMap["4-1"]+shownMap["4-2"]+shownMap["4-3"]+shownMap["4-4"]+shownMap["4-5"]+shownMap["4-6"]+shownMap["4-7"]+shownMap["4-8"]+"\n"+shownMap["5-0"]+shownMap["5-1"]+shownMap["5-2"]+shownMap["5-3"]+shownMap["5-4"]+shownMap["5-5"]+shownMap["5-6"]+shownMap["5-7"]+shownMap["5-8"]+"\n"+shownMap["6-0"]+shownMap["6-1"]+shownMap["6-2"]+shownMap["6-3"]+shownMap["6-4"]+shownMap["6-5"]+shownMap["6-6"]+shownMap["6-7"]+shownMap["6-8"]+"\n"+shownMap["7-0"]+shownMap["7-1"]+shownMap["7-2"]+shownMap["7-3"]+shownMap["7-4"]+shownMap["7-5"]+shownMap["7-6"]+shownMap["7-7"]+shownMap["7-8"]+"\n"+shownMap["8-0"]+shownMap["8-1"]+shownMap["8-2"]+shownMap["8-3"]+shownMap["8-4"]+shownMap["8-5"]+shownMap["8-6"]+shownMap["8-7"]+shownMap["8-8"]+"\n"+shownMap["9-0"]+shownMap["9-1"]+shownMap["9-2"]+shownMap["9-3"]+shownMap["9-4"]+shownMap["9-5"]+shownMap["9-6"]+shownMap["9-7"]+shownMap["9-8"]+"\n"+shownMap["10-0"]+shownMap["10-1"]+shownMap["10-2"]+shownMap["10-3"]+shownMap["10-4"]+shownMap["10-5"]+shownMap["10-6"]+shownMap["10-7"]+shownMap["10-8"]+"\n\n")
	print("You made it to the end!")


main()
