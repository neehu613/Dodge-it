import pygame
import time
import random

#color definitions
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,215,0)

#global game variables
winW = 1200
winH = 700
i = 1	#to keep track of the score as a multiple of 100 to manipulate the gamelevel
pygame.init()
gameDisplay = pygame.display.set_mode((winW, winH))
pygame.display.set_caption("Dodge the cars")
clock = pygame.time.Clock()
FPS = 30
smallfont = pygame.font.SysFont(None, 30)
mediumfont = pygame.font.SysFont(None, 50)
largefont = pygame.font.SysFont(None, 80)


#image loading
bg = pygame.image.load("images/background.png")
bg = pygame.transform.scale(bg, (1200, 700))

playerCar = pygame.image.load("images/playerCar.png")
playerCar = pygame.transform.scale(playerCar, (80, 160))

enemyCar1 = pygame.image.load("images/car1.png")
enemyCar1 = pygame.transform.scale(enemyCar1, (80, 160))

enemyCar2 = pygame.image.load("images/car2.png")
enemyCar2 = pygame.transform.scale(enemyCar2, (80, 160))

enemyCar3 = pygame.image.load("images/car3.png")
enemyCar3 = pygame.transform.scale(enemyCar3, (80, 160))

enemyCar4 = pygame.image.load("images/car4.png")
enemyCar4 = pygame.transform.scale(enemyCar4, (80, 160))

enemyCar5 = pygame.image.load("images/car5.png")
enemyCar5 = pygame.transform.scale(enemyCar5, (80, 160))

enemyCar6 = pygame.image.load("images/car6.png")
enemyCar6 = pygame.transform.scale(enemyCar6, (80, 160))

truck1 = pygame.image.load("images/truck1.jpg")
truck1 = pygame.transform.scale(truck1, (100, 200))

truck3 = pygame.image.load("images/truck3.jpg")
truck3 = pygame.transform.scale(truck3, (100, 200))

#audio files
bgMusic = pygame.mixer.music.load('sound/bg.mp3')
crash = pygame.mixer.Sound('sound/crash.wav')
coin = pygame.mixer.Sound('sound/coin.wav')

def gameQuit():
	pygame.quit()
	quit()

def printMessage(msg, color, font, yLoc=0):
	textSurface = font.render(msg, True, color)
	textRect = textSurface.get_rect()
	textRect.center = (winW/2), (winH/2)+yLoc
	gameDisplay.blit(textSurface, textRect)
	

def score(dodged, coins, level):
	spaces = str(10 * " ")
	totalCoinsScore = coins * 10
	totalDodgedScore = dodged * 5
	totalScore = totalCoinsScore + totalDodgedScore
	pygame.draw.rect(gameDisplay, black, [0,0,150, 120])
	text = smallfont.render("Score -  "+ str(totalScore), True, blue)
	gameDisplay.blit(text, [20, 15])
	text = smallfont.render("Dodged -  "+ str(dodged), True, blue)
	gameDisplay.blit(text, [20, 40])
	text = smallfont.render("Coins -  "+ str(coins), True, blue)
	gameDisplay.blit(text, [20, 75])
	text = smallfont.render("Level -  "+ str(level), True, blue)
	gameDisplay.blit(text, [20, 100])
	pygame.display.update()
	
def instructions():
	instructionPage = True	
	gameDisplay.fill(white)
	
	while instructionPage == True:
		msg = "The main motto of this game is to dodge the cars and pick up the coins"
		msg1 = "Controls are as follows"
		msg2 = "LEFT KEY to move left"
		msg3 = "RIGHT KEY to move right"
		msg4 = "Press P to play and q to Quit"
		msg5 = "While playing, press P to pause"
		printMessage(msg, blue, mediumfont, -50)
		printMessage(msg1, black, smallfont)
		printMessage(msg2, black, smallfont, 30)
		printMessage(msg3, black, smallfont, 60)
		printMessage(msg4, red, smallfont, 150)
		printMessage(msg5, red, smallfont, 180)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameQuit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					instructionPage = False
				elif event.key == pygame.K_q:
					gameQuit()
		
		clock.tick(10)
		pygame.display.update()


def gameIntro():
	intro = True
	
	while intro:
		gameDisplay.fill(white)
		msg = "Dodge the cars"
		msg1 = "Press I to view the instructions to play and q to Quit"
		printMessage(msg, blue, largefont, -50)
		printMessage(msg1, black, smallfont, +50)
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameQuit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_i:
					instructions()
					intro = False
				elif event.key == pygame.K_q:
					gameQuit()
		
		clock.tick(10)
		pygame.display.update()

def gamePaused():
	pygame.mixer.music.pause()
	gameDisplay.fill(white)
	printMessage("Game Paused", red, largefont, -20)
	printMessage("Press P to continue playing and Q to quit", black, smallfont, 70)
	pygame.display.update()
	
	paused = True

	while paused == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameQuit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					pygame.mixer.music.unpause()
					paused = False
				if event.key == pygame.K_q:
					gameQuit()

	
	
	clock.tick(10)

def popUpLevel(level):
	msg = "Level = " + str(level)
	printMessage(msg, blue, largefont)
	pygame.display.update()
	clock.tick(20)
	time.sleep(1)
	gameDisplay.fill(white)
	pygame.display.update()

def gameLoop():
	#variable declarations
	gameOver = gameExit = False
	characterW = 80
	characterH = 160
	characterX = winW/2
	characterY = winH*0.8
	x_change = 0
	x_disp = 30
	speed = 0

	bgX = 0
	bgY = 0
	bgX1 = 0
	bgY1 = -winH
	bgY_change = 10

	randCar = random.randrange(1,9)	
	
	object_height = 160
	object_width = 80
	y_change = 30
	objectY = -500
	objectX = random.randrange(200, winW-175-object_width)
	dodged = 0
	
	coin_radius = 30
	coinX = random.randrange(200, winW-175-coin_radius)
	coinY = -1000
	y_change_coin = random.randrange(10, 50)
	coins = 0
	
	level = 1
	theScore = 0
	global highScore

	pygame.mixer.music.play(-1)

	gameDisplay.fill(white)
	popUpLevel(level)

	global i

	while not gameExit:
		#game over event handling
		while gameOver == True:


			gameDisplay.fill(white)
			printMessage("You are dead", red, largefont)
			printMessage("Number of cars dodged: "+ str(dodged), black, smallfont, 80)
			printMessage("Number of coins collected: "+ str(coins), black, smallfont, 110)
			printMessage("Your score: "+ str(theScore), black, smallfont, 140)
			printMessage("Press P to play and q to Quit", black, smallfont, 250)
			

			with open("highScore.txt") as f:
				highScore = int(f.read())
				if theScore >= highScore:
					highScore = theScore
					printMessage("New High Score: "+ str(highScore), black, smallfont, 300)		
			with open("highScore.txt", "w") as f:
				f.write(str(highScore))
			
			printMessage("High Score: "+ str(highScore), black, smallfont, 170)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameQuit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						pygame.mixer.music.play(-1)
						x_change = 0
						i = 1
						speed = 0
						characterX = winW/2
						objectY = -500
						objectX = random.randrange(200, winW-175-object_width)
						coins = dodged = theScore = 0
						level = 1
						gameOver = False
					elif event.key == pygame.K_q:
						gameQuit()
			clock.tick(10)
			pygame.display.update()
			
		
		#event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameQuit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -x_disp - speed
				elif event.key == pygame.K_RIGHT:
					x_change = x_disp + speed
				elif event.key == pygame.K_p:
					gamePaused()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		
		characterX += x_change
		objectY += y_change
		coinY += y_change_coin
		bgY1 += bgY_change
		bgY += bgY_change



		#game rendering
		gameDisplay.fill(white)
		gameDisplay.blit(bg, (bgX,bgY))
		gameDisplay.blit(bg, (bgX1, bgY1))
		gameDisplay.blit(playerCar, (characterX, characterY))
		

		if randCar == 1:
			gameDisplay.blit(enemyCar1, (objectX,objectY))
		elif randCar == 2:
			gameDisplay.blit(enemyCar2, (objectX,objectY))
		elif randCar == 3:
			gameDisplay.blit(enemyCar3, (objectX,objectY))
		elif randCar == 4:
			gameDisplay.blit(enemyCar4, (objectX,objectY))
		elif randCar == 5:
			gameDisplay.blit(enemyCar5, (objectX,objectY))
		elif randCar == 6:
			gameDisplay.blit(enemyCar6, (objectX,objectY))
		elif randCar == 7:
			gameDisplay.blit(truck1, (objectX,objectY))
		elif randCar == 8:
			gameDisplay.blit(truck3, (objectX,objectY))


		pygame.draw.circle(gameDisplay,yellow, [coinX, coinY], coin_radius)
		score(dodged, coins, level)
		pygame.display.update()
		clock.tick(FPS)
		
		#gameLogic
		if characterX <= 200 or characterX >= winW-175-characterW:
			pygame.mixer.music.stop()
			pygame.mixer.Sound.play(crash)
			time.sleep(1.5)
			gameOver = True
		
		if objectY > winH:
			objectX = random.randrange(200, winW - 200 -object_width)
			objectY = -500
			dodged += 1
			'''
			theScore = (coins * 10) + (dodged * 5)
			if theScore >= 100*i:
					i+=1
					level += 1
					speed += 10
					popUpLevel(level)
			'''
			randCar = random.randrange(1,9)
		
		if objectY+object_height >= characterY:
			if objectX+object_width >= characterX and objectX <= characterX+characterW:
				pygame.mixer.music.stop()
				pygame.mixer.Sound.play(crash)
				time.sleep(1.5)
				gameOver = True
		
		if coinY > winH:
			coinX = random.randrange(200, winW - 175 - coin_radius)
			coinY = -random.randrange(300, 1000)
			y_change_coin = random.randrange(10, 50)
			

		if coinY+coin_radius >= characterY:
			if characterX + characterW >= coinX-coin_radius and characterX <= coinX+coin_radius:
				coins += 1
				theScore = (coins * 10) + (dodged * 5)
				coinX = random.randrange(200, winW -175- coin_radius)
				coinY = -random.randrange(300, 1000)
				y_change_coin = random.randrange(10, 50)
				pygame.mixer.Sound.play(coin)
				if theScore >= 100*i:
					i+=1
					y_change +=10
					level += 1
					speed += 10
					popUpLevel(level)

		if bgY >= winH:
				bgY = -winH
		if bgY1 >= winH:
				bgY1 = -winH

#function calls
gameIntro()
gameLoop()
gameQuit()