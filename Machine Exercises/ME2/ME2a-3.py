#Round and Round

import random

pts_you = 0
pts_foe = 0
roundd = 1

pts_towin = int(input("Number of pts. to win:"))

while pts_you != pts_towin and pts_foe != pts_towin:
	print("Round:", roundd)	
	print("You:", pts_you)
	print("Foe:", pts_foe)

	foe = random.choice(["rock", "paper", "scissors"])
	you = input("You:")	
	print("AI:" + foe)


	if you == foe:
		print("Draw.")
	elif (you == "rock" and foe == "scissors") or ( you == "paper" and foe == "rock") or ( you == "scissors" and foe == "paper"):
		print("You win!")
		pts_you +=1
	else:
		print("loser hehe")
		pts_foe +=1
	
	print()
	roundd +=1

if pts_you == pts_foe:
	print("The result is a DRAW!")
elif pts_you > pts_foe:
	print("YOU win!")
else:
	print("FOE win!")

print("Overall Points")
print("You:", pts_you)
print("Foe:", pts_foe)
	

