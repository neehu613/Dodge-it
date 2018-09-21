from cx_Freeze import setup, Executable

setup(
	name = "Dodge the Cars",
	options = {"build_exe": {"packages":["pygame"], 
							 "include_files": ["background.png", "bg.mp3", "car1.png", "car2.png", "car3.png", "car4.png", "car5.png", "car6.png", "crash.wav", "coin.wav", "highScore.txt", "playerCar.png", "truck1.jpg", "truck3.jpg"]}},
	description = "Dodge the coins and pick up the coins",
	executables = [Executable("dodge.py")]
	)