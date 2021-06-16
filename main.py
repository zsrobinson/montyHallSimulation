import random
import time

switchWins = 0
stayWins = 0

iterations = round(int(input("Iterations  : "))/2)

def game(switch):
	global switchWins
	global stayWins
	win = random.randint(1,3)
	selected = random.randint(1,3)
	if switch == True:
		doors = [1,2,3]
		doors.remove(selected)
		try:
			doors.remove(win)
		except:
			pass
		removedDoor = random.choice(doors)
		moreDoors = [1,2,3]
		moreDoors.remove(selected)
		try:
			moreDoors.remove(removedDoor)
		except:
			pass
		selected = moreDoors[0]
	if selected == win:
		if switch == True:
			switchWins += 1
		else:
			stayWins += 1

startTime = time.time()

for i in range(iterations):
	game(True)

for i in range(iterations):
	game(False)

print("Switch Wins : "+str(round(100*(switchWins/iterations),2))+"%")

print("Stay Wins   : "+str(round(100*(stayWins/iterations),2))+"%")

print('Time        : ' + str(round(time.time()-startTime,2))+" sec")