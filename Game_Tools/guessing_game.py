import random

def newGame(trial):
	trial = str(input("Do you want to play again? "))
	return(trial)
                
def guessingGame(trial):
	ans = random.randint(1,101)

	guess = int(input("Guess a number from 1 to 100 "))

	while guess!= ans:
		if guess > (ans+30):
			print("Way over! ")
		elif guess < (ans-30):
			print("Way under! ")
		elif guess > (ans+10):
			print("Too high. ")
		elif guess < (ans-10):
			print("Too low. ")
		elif guess > ans:
			print("Just over! ")
		elif guess < ans:
			print("Just under! ")
		guess = int(input("Try again! "))
	print("On the money!")
	newGame(trial)
	return(trial)

def main():
	trial="yes"
	while trial == "yes" or "Yes" or "y" or "Y":
		trial = guessingGame(trial)
	exit()
        
main()