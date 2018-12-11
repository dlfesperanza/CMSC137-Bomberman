'''
!!! Click anywhere on the map first before pressing keys
Controls
w: up
a: left
s: down
d: right
space: drop bomb
'''
import subprocess
from tkinter import *
from PIL import Image, ImageTk
from threading import Timer

def key(event):
	action(event.char)

def callback(event):
    startFrame.focus_set()

def printMap():
	global mapData

	m = {}
	m = mapData
	print("\n")
	for i in range(0,len(mapData)):
		print(m[i][0],m[i][1],m[i][2],m[i][3],m[i][4],m[i][5],m[i][6],m[i][7],m[i][8],m[i][9],m[i][10],m[i][11],m[i][12],m[i][13],m[i][14])

def updateLabel(xpos,ypos,img):
	global labels
	global startFrame

	labels[xpos][ypos] = Label(startFrame, image=img)
	labels[xpos][ypos].image = img
	labels[xpos][ypos].place(x=(ypos*18),y=xpos*18)

	startFrame.pack(side=LEFT)

def switchLabels1(xpos,ypos,zpos):
	global labels
	global startFrame

	tempLabel = Label(startFrame)
	tempLabel = labels[playerPos[0]][playerPos[1]]
	labels[xpos][ypos] = labels[xpos][zpos]
	labels[xpos][zpos] = tempLabel
	labels[xpos][ypos].place(x=(ypos)*18,y=xpos*18)
	labels[xpos][zpos].place(x=(zpos)*18,y=xpos*18)

	startFrame.pack(side=LEFT)

def switchLabels2(xpos,ypos,zpos):
	global labels
	global startFrame

	tempLabel = Label(startFrame)
	tempLabel = labels[playerPos[0]][playerPos[1]]
	labels[xpos][ypos] = labels[zpos][ypos]
	labels[zpos][ypos] = tempLabel
	labels[xpos][ypos].place(x=(ypos)*18,y=xpos*18)
	labels[zpos][ypos].place(x=(ypos)*18,y=zpos*18)

	startFrame.pack(side=LEFT)

def grassLabel(x1,y1,x2,y2):
	global mapData
	global startFrame
	global labels
	global bombPos

	if (x2>=0 and x2<=12) and (y2>=0 and y2<=14):
		grass = Image.open("./images/grass.png")
		grassicon = ImageTk.PhotoImage(grass)
		labels[x1][y1] = Label(startFrame, image=grassicon)
		labels[x1][y1].image = grassicon
		labels[x1][y1].place(x=y1*18,y=x1*18)

		if mapData[x2][y2] != "w" and mapData[x2][y2] != "m":
			labels[x2][y2] = Label(startFrame, image=grassicon)
			labels[x2][y2].image = grassicon
			labels[x2][y2].place(x=(y2)*18,y=(x2)*18)

		mapData[x1][y1] = 'g'
		mapData[x2][y2] = 'g'
		startFrame.pack(side=LEFT)

def updatePowerup(powerup):
	global powerups

	if powerup == '1':
		powerups[0] = 1
	elif powerup == '2':
		powerups[1] = 1
	elif powerup == '3':
		powerups[2] = 1
	elif powerup == '4':
		powerups[3] = 1
	print(powerups)

def action(move):
	global mapData
	global playerPos
	global startFrame
	global labels
	global lastMove
	global bombPos

	bomb = Image.open("./images/bomb.png")
	bombicon = ImageTk.PhotoImage(bomb)
	player = Image.open("./images/player1.png")
	playericon = ImageTk.PhotoImage(player)
	grass = Image.open("./images/grass.png")
	grassicon = ImageTk.PhotoImage(grass)

	if move == 'd': 	#right
		if mapData[playerPos[0]][playerPos[1]+1] == 'g':
			if lastMove == " ":
				updateLabel(playerPos[0],playerPos[1],bombicon)
				updateLabel(playerPos[0],playerPos[1]+1,playericon)
				
				lastMove = '*'
			else:
				updateLabel(playerPos[0],playerPos[1],grassicon)
				updateLabel(playerPos[0],playerPos[1]+1,playericon)

			mapData[playerPos[0]][playerPos[1]+1] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[1] = playerPos[1] + 1
		elif mapData[playerPos[0]][playerPos[1]+1] == '1' or mapData[playerPos[0]][playerPos[1]+1] == '2' or mapData[playerPos[0]][playerPos[1]+1] == '3' or mapData[playerPos[0]][playerPos[1]+1] == '4':
			updatePowerup(mapData[playerPos[0]][playerPos[1]+1])
			updateLabel(playerPos[0],playerPos[1],grassicon)
			updateLabel(playerPos[0],playerPos[1]+1,grassicon)
			updateLabel(playerPos[0],playerPos[1]+1,playericon)

			mapData[playerPos[0]][playerPos[1]+1] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[1] = playerPos[1] + 1

	elif move == 'a': 	#left
		if mapData[playerPos[0]][playerPos[1]-1] == 'g':
			if lastMove == " ":
				updateLabel(playerPos[0],playerPos[1],bombicon)
				updateLabel(playerPos[0],playerPos[1]-1,playericon)

				lastMove = '*'
			else:
				updateLabel(playerPos[0],playerPos[1],grassicon)
				updateLabel(playerPos[0],playerPos[1]-1,playericon)

			mapData[playerPos[0]][playerPos[1]-1] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[1] = playerPos[1] - 1
		elif mapData[playerPos[0]][playerPos[1]-1] == '1' or mapData[playerPos[0]][playerPos[1]-1] == '2' or mapData[playerPos[0]][playerPos[1]-1] == '3' or mapData[playerPos[0]][playerPos[1]-1] == '4':
			updatePowerup(mapData[playerPos[0]][playerPos[1]-1])
			updateLabel(playerPos[0],playerPos[1],grassicon)
			updateLabel(playerPos[0],playerPos[1]-1,grassicon)
			updateLabel(playerPos[0],playerPos[1]-1,playericon)

			mapData[playerPos[0]][playerPos[1]-1] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[1] = playerPos[1] - 1
	elif move == 'w': 	#up
		if mapData[playerPos[0]-1][playerPos[1]] == 'g':
			if lastMove == " ":
				updateLabel(playerPos[0],playerPos[1],bombicon)
				updateLabel(playerPos[0]-1,playerPos[1],playericon)

				lastMove = '*'
			else:
				updateLabel(playerPos[0],playerPos[1],grassicon)
				updateLabel(playerPos[0]-1,playerPos[1],playericon)

			mapData[playerPos[0]-1][playerPos[1]] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[0] = playerPos[0] - 1
		elif mapData[playerPos[0]-1][playerPos[1]] == '1' or mapData[playerPos[0]-1][playerPos[1]] == '2' or mapData[playerPos[0]-1][playerPos[1]] == '3' or mapData[playerPos[0]-1][playerPos[1]] == '4':
			updatePowerup(mapData[playerPos[0]-1][playerPos[1]])
			updateLabel(playerPos[0],playerPos[1],grassicon)
			updateLabel(playerPos[0]-1,playerPos[1],grassicon)
			updateLabel(playerPos[0]-1,playerPos[1],playericon)

			mapData[playerPos[0]-1][playerPos[1]] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[0] = playerPos[0] - 1
	elif move == 's': 	#down
		if mapData[playerPos[0]+1][playerPos[1]] == 'g':
			if lastMove == " ":
				updateLabel(playerPos[0],playerPos[1],bombicon)
				updateLabel(playerPos[0]+1,playerPos[1],playericon)

				lastMove = '*'
			else:
				updateLabel(playerPos[0],playerPos[1],grassicon)
				updateLabel(playerPos[0]+1,playerPos[1],playericon)

			mapData[playerPos[0]+1][playerPos[1]] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[0] = playerPos[0] + 1
		elif mapData[playerPos[0]+1][playerPos[1]] == '1' or mapData[playerPos[0]+1][playerPos[1]] == '2' or mapData[playerPos[0]+1][playerPos[1]] == '3' or mapData[playerPos[0]+1][playerPos[1]] == '4':
			updatePowerup(mapData[playerPos[0]+1][playerPos[1]])
			updateLabel(playerPos[0],playerPos[1],grassicon)
			updateLabel(playerPos[0]+1,playerPos[1],grassicon)
			updateLabel(playerPos[0]+1,playerPos[1],playericon)
			

			mapData[playerPos[0]+1][playerPos[1]] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[0] = playerPos[0] + 1
	elif move == " ": #place bomb
		bombPos[0] = playerPos[0]
		bombPos[1] = playerPos[1]
		placebomb = Image.open("./images/placebomb1.png")
		placebombicon = ImageTk.PhotoImage(placebomb)
		labels[playerPos[0]][playerPos[1]] = Label(startFrame, image=placebombicon)
		labels[playerPos[0]][playerPos[1]].image = placebombicon
		labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1]*18),y=playerPos[0]*18)
		if powerups[1] == 1: #if fuse powerup obtained
			labels[playerPos[0]][playerPos[1]].after(1000,explodeBomb)
		else:
			labels[playerPos[0]][playerPos[1]].after(2000,explodeBomb)

		startFrame.pack(side=LEFT)
		lastMove = " "
	printMap()
	window.mainloop()

def initMap():
	global startFrame
	global mapData
	global labels

	startFrame.pack_forget()
	startFrame = Frame(window,width = 300, height = 300)
	startFrame.configure(background="white")

	labels = {}
	xpos = 0
	
	for i in range(0,len(mapData)):
		labels[i] = {}
		ypos = 0
		for j in range(0,len(mapData[i])):
			if mapData[i][j] == 'w':
				wall1 = Image.open("./images/wall1.png")
				wallicon = ImageTk.PhotoImage(wall1)
				labels[i][j] = Label(startFrame, image=wallicon)
				labels[i][j].image = wallicon
				labels[i][j].place(x=ypos,y=xpos)
			elif mapData[i][j] == 'm':
				wall2 = Image.open("./images/wall2.png")
				wall2icon = ImageTk.PhotoImage(wall2)
				labels[i][j] = Label(startFrame, image=wall2icon)
				labels[i][j].image = wall2icon
				labels[i][j].place(x=ypos,y=xpos)
			elif mapData[i][j] == 'g':
				grass = Image.open("./images/grass.png")
				grassicon = ImageTk.PhotoImage(grass)
				labels[i][j] = Label(startFrame, image=grassicon)
				labels[i][j].image = grassicon
				labels[i][j].place(x=ypos,y=xpos)
			elif mapData[i][j] == 'p':
				player = Image.open("./images/player1.png")
				playericon = ImageTk.PhotoImage(player)
				labels[i][j] = Label(startFrame, image=playericon)
				labels[i][j].image = playericon
				labels[i][j].place(x=ypos,y=xpos)
			elif mapData[i][j] == 'b':
				box = Image.open("./images/box.png")
				boxicon = ImageTk.PhotoImage(box)
				labels[i][j] = Label(startFrame, image=boxicon)
				labels[i][j].image = boxicon
				labels[i][j].place(x=ypos,y=xpos)
			elif mapData[i][j] == '1':
				gunpowder = Image.open("./images/gunpowder.png")
				gunpowdericon = ImageTk.PhotoImage(gunpowder)
				labels[i][j] = Label(startFrame, image=gunpowdericon)
				labels[i][j].image = gunpowdericon
				labels[i][j].place(x=ypos,y=xpos)
			elif mapData[i][j] == '2':
				fuse = Image.open("./images/fuse.png")
				fuseicon = ImageTk.PhotoImage(fuse)
				labels[i][j] = Label(startFrame, image=fuseicon)
				labels[i][j].image = fuseicon
				labels[i][j].place(x=ypos,y=xpos)
			elif mapData[i][j] == '3':
				shoes = Image.open("./images/shoes.png")
				shoesicon = ImageTk.PhotoImage(shoes)
				labels[i][j] = Label(startFrame, image=shoesicon)
				labels[i][j].image = shoesicon
				labels[i][j].place(x=ypos,y=xpos)
			elif mapData[i][j] == '4':
				shield = Image.open("./images/shield.png")
				shieldicon = ImageTk.PhotoImage(shield)
				labels[i][j] = Label(startFrame, image=shieldicon)
				labels[i][j].image = shieldicon
				labels[i][j].place(x=ypos,y=xpos)
			ypos = ypos + 18
		xpos = xpos + 18
	startFrame.bind("<Key>", key)
	startFrame.bind("<Button-1>", callback)
	startFrame.pack(side=LEFT)

def start(): 
	global mapData
	global startFrame
	global playerPos
	global backBtn
	global lastMove
	global bombPos
	global powerups

	powerups = [0,0,0,0] #empty power ups initially
	lastMove = '*'
	homeFrame.pack_forget()
	window.geometry("500x300")
	startFrame = Frame(window,width = 600, height = 350)
	
	backBtn = Button(window, text = "Quit", command = lambda: returnMenu(startFrame), bg = "#C0C0C0", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	
	backBtn.place(x=0,y=18,anchor=CENTER)
	backBtn.pack()
	
	mapData = loadFileReader() #reads the map file and writes to a 2d array
	playerPos = {}
	playerPos[0] = 1 #x position
	playerPos[1] = 1 #y position
	bombPos = {}

	initMap()
	window.mainloop()
	
def explodeBomb():
	global mapData
	global startFrame
	global labels
	global bombPos
	global powerups

	if powerups[0] == 0: #no gunpowder powerup
		grassLabel(bombPos[0],bombPos[1],bombPos[0]-1,bombPos[1])
		grassLabel(bombPos[0],bombPos[1],bombPos[0],bombPos[1]-1)
		grassLabel(bombPos[0],bombPos[1],bombPos[0],bombPos[1]+1)
		grassLabel(bombPos[0],bombPos[1],bombPos[0]+1,bombPos[1])
	else:
		grassLabel(bombPos[0],bombPos[1],bombPos[0]-2,bombPos[1])
		grassLabel(bombPos[0],bombPos[1],bombPos[0]-1,bombPos[1]-1)
		grassLabel(bombPos[0],bombPos[1],bombPos[0]-1,bombPos[1]+1)
		grassLabel(bombPos[0],bombPos[1],bombPos[0],bombPos[1]-2)
		grassLabel(bombPos[0],bombPos[1],bombPos[0],bombPos[1]+2)
		grassLabel(bombPos[0],bombPos[1],bombPos[0]+1,bombPos[1]-1)
		grassLabel(bombPos[0],bombPos[1],bombPos[0]+1,bombPos[1]+1)
		grassLabel(bombPos[0],bombPos[1],bombPos[0]+2,bombPos[1])

def howToPlay():
	homeFrame.pack_forget()
	
	howFrame = Frame(window, width = 25)
	photo = ImageTk.PhotoImage(Image.open("./images/howtoplay-bg.png"))
	picLbl = Label(howFrame, image=photo,width=600,height=505)
	picLbl.place(x=1, y=1, relwidth=1, relheight=1)
	backBtn = Button(picLbl, text = "Back", command = lambda: returnMenu(howFrame), bg = "#C0C0C0", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	picLbl.pack()
	backBtn.pack()
	backBtn.place(x=60,y=18,anchor=CENTER)
	
	howFrame.pack()
	window.mainloop()

def highscores():
	homeFrame.pack_forget()
	
	hsFrame = Frame(window, width = 25)
	photo = ImageTk.PhotoImage(Image.open("./images/highscore-bg.png"))
	picLbl = Label(hsFrame, image=photo,width=600,height=505)
	picLbl.place(x=1, y=1, relwidth=1, relheight=1)
	backBtn = Button(picLbl, text = "Back", command = lambda: returnMenu(hsFrame), bg = "#C0C0C0", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	picLbl.pack()
	backBtn.pack()
	backBtn.place(x=60,y=18,anchor=CENTER)
	
	hsFrame.pack()
	window.mainloop()

def exit(): #For Exit button; exits the GUI/game
	window.destroy()

def returnMenu(frame): #Forgets previous frame
	backBtn.pack_forget()
	frame.pack_forget()
	homeFrame.pack()
	window.geometry("600x505")

'''============================================================================'''
def loadFileReader(): #Reads the map
	mapData=[]
	fileRead=open("map.csv","r")
	
	for line in fileRead:
		line = line[:-1]
		line=line.split(",")
		mapData.append(line)
	return mapData

class chatClass():
    def __init__(self):
        self.child = subprocess.Popen([sys.executable, '../chat.py'])
    def onClose( self , evt ):
        self.child.wait()
        self.exit();

'''============================================================================'''
sys.setrecursionlimit(1500)
window = Tk()
window.title("Bomberman")
window.geometry("600x505")
window.configure(background = "white")
'''===================================Game Menu================================'''
homeFrame = Frame(window, width = 600, height = 505)
#Background picture
photo = ImageTk.PhotoImage(Image.open("./images/background.png"))
picLbl = Label(homeFrame, image=photo,width=600,height=505)
picLbl.place(x=1, y=1, relwidth=1, relheight=1)
#Menu Buttons
startBtn = Button(picLbl, text = "Start", fg = "red", width = 8, font = ("Quicksand", 12),command=start, bg="white",relief="groove")
howtoplayBtn = Button(picLbl, text = "How to Play", fg = "red", width = 8, font = ("Quicksand", 12),command=howToPlay, bg="white",relief="groove")
highscoreBtn = Button(picLbl, text = "High Scores", fg = "red", width = 8, font = ("Quicksand", 12),command=highscores, bg="white",relief="groove")
exitBtn = Button(picLbl, text = "Exit", fg = "red", width = 8, font = ("Quicksand", 12), command = exit, bg="white",relief="groove")
#Pack
picLbl.pack()
startBtn.pack()
startBtn.place(x=300,y=260,anchor=CENTER)
howtoplayBtn.pack()
howtoplayBtn.place(x=300,y=300,anchor=CENTER)
highscoreBtn.pack()
highscoreBtn.place(x=300,y=340,anchor=CENTER)
exitBtn.pack()
exitBtn.place(x=300,y=380,anchor=CENTER)
homeFrame.pack()

chatvar = chatClass()
window.mainloop()

'''============================================================================'''
