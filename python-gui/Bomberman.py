'''
!!! Click anywhere on the map first before pressing keys
Controls
w: up
a: left
s: down
d: right
space: drop bomb
'''

from tkinter import *
from PIL import Image, ImageTk
from threading import Timer

def key(event):
	action(event.char)

def callback(event):
    startFrame.focus_set()

def action(move):
	global mapData
	global playerPos
	global startFrame
	global labels
	global lastMove
	global bombPos

	tempLabel = Label(startFrame)
	bomb = Image.open("./images/bomb.png")
	bombicon = ImageTk.PhotoImage(bomb)
	player = Image.open("./images/player1.png")
	playericon = ImageTk.PhotoImage(player)

	if move == 'd': 	#right
		if mapData[playerPos[0]][playerPos[1]+1] == 'g':
			if lastMove == " ":
				labels[playerPos[0]][playerPos[1]] = Label(startFrame, image=bombicon)
				labels[playerPos[0]][playerPos[1]].image = bombicon
				labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1]*18),y=playerPos[0]*18)

				labels[playerPos[0]][playerPos[1]+1] = Label(startFrame, image=playericon)
				labels[playerPos[0]][playerPos[1]+1].image = playericon
				labels[playerPos[0]][playerPos[1]+1].place(x=(playerPos[1]+1)*18,y=playerPos[0]*18)
				startFrame.pack(side=LEFT)
				
				lastMove = '*'
			else:
				tempLabel = labels[playerPos[0]][playerPos[1]]
				labels[playerPos[0]][playerPos[1]] = labels[playerPos[0]][playerPos[1]+1]
				labels[playerPos[0]][playerPos[1]+1] = tempLabel
				labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1])*18,y=playerPos[0]*18)
				labels[playerPos[0]][playerPos[1]+1].place(x=(playerPos[1]+1)*18,y=playerPos[0]*18)

				startFrame.pack(side=LEFT)

			mapData[playerPos[0]][playerPos[1]+1] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[1] = playerPos[1] + 1
	elif move == 'a': 	#left
		if mapData[playerPos[0]][playerPos[1]-1] == 'g':
			if lastMove == " ":
				labels[playerPos[0]][playerPos[1]] = Label(startFrame, image=bombicon)
				labels[playerPos[0]][playerPos[1]].image = bombicon
				labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1]*18),y=playerPos[0]*18)

				labels[playerPos[0]][playerPos[1]-1] = Label(startFrame, image=playericon)
				labels[playerPos[0]][playerPos[1]-1].image = playericon
				labels[playerPos[0]][playerPos[1]-1].place(x=(playerPos[1]-1)*18,y=playerPos[0]*18)
				lastMove = '*'
			else:
				tempLabel = labels[playerPos[0]][playerPos[1]]
				labels[playerPos[0]][playerPos[1]] = labels[playerPos[0]][playerPos[1]-1]
				labels[playerPos[0]][playerPos[1]-1] = tempLabel
				labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1])*18,y=playerPos[0]*18)
				labels[playerPos[0]][playerPos[1]-1].place(x=(playerPos[1]-1)*18,y=playerPos[0]*18)

			startFrame.pack(side=LEFT)

			mapData[playerPos[0]][playerPos[1]-1] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[1] = playerPos[1] - 1
	elif move == 'w': 	#up
		if mapData[playerPos[0]-1][playerPos[1]] == 'g':
			if lastMove == " ":
				labels[playerPos[0]][playerPos[1]] = Label(startFrame, image=bombicon)
				labels[playerPos[0]][playerPos[1]].image = bombicon
				labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1]*18),y=playerPos[0]*18)

				labels[playerPos[0]-1][playerPos[1]] = Label(startFrame, image=playericon)
				labels[playerPos[0]-1][playerPos[1]].image = playericon
				labels[playerPos[0]-1][playerPos[1]].place(x=(playerPos[1])*18,y=(playerPos[0]-1)*18)
				lastMove = '*'
			else:
				tempLabel = labels[playerPos[0]][playerPos[1]]
				labels[playerPos[0]][playerPos[1]] = labels[playerPos[0]-1][playerPos[1]]
				labels[playerPos[0]-1][playerPos[1]] = tempLabel
				labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1])*18,y=playerPos[0]*18)
				labels[playerPos[0]-1][playerPos[1]].place(x=(playerPos[1])*18,y=(playerPos[0]-1)*18)

			startFrame.pack(side=LEFT)

			mapData[playerPos[0]-1][playerPos[1]] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[0] = playerPos[0] - 1
	elif move == 's': 	#down
		if mapData[playerPos[0]+1][playerPos[1]] == 'g':
			if lastMove == " ":
				labels[playerPos[0]][playerPos[1]] = Label(startFrame, image=bombicon)
				labels[playerPos[0]][playerPos[1]].image = bombicon
				labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1]*18),y=playerPos[0]*18)

				labels[playerPos[0]+1][playerPos[1]] = Label(startFrame, image=playericon)
				labels[playerPos[0]+1][playerPos[1]].image = playericon
				labels[playerPos[0]+1][playerPos[1]].place(x=(playerPos[1])*18,y=(playerPos[0]+1)*18)
				lastMove = '*'
			else:
				tempLabel = labels[playerPos[0]][playerPos[1]]
				labels[playerPos[0]][playerPos[1]] = labels[playerPos[0]+1][playerPos[1]]
				labels[playerPos[0]+1][playerPos[1]] = tempLabel
				labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1]*18),y=playerPos[0]*18)
				labels[playerPos[0]+1][playerPos[1]].place(x=(playerPos[1]*18),y=(playerPos[0]+1)*18)

			startFrame.pack(side=LEFT)

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
		labels[playerPos[0]][playerPos[1]].after(3000,explodeBomb)
		print("*")


		startFrame.pack(side=LEFT)
		lastMove = " "
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

	lastMove = '*'
	homeFrame.pack_forget()
	window.geometry("500x300")
	startFrame = Frame(window,width = 600, height = 350)
	
	backBtn = Button(window, text = "Quit", command = lambda: returnMenu(startFrame), bg = "silver", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	
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

	grass = Image.open("./images/grass.png")
	grassicon = ImageTk.PhotoImage(grass)
	labels[bombPos[0]][bombPos[1]] = Label(startFrame, image=grassicon)
	labels[bombPos[0]][bombPos[1]].image = grassicon
	labels[bombPos[0]][bombPos[1]].place(x=bombPos[1]*18,y=bombPos[0]*18)

	if mapData[bombPos[0]-1][bombPos[1]-1] != "w" and mapData[bombPos[0]-1][bombPos[1]-1] != "m":
		labels[bombPos[0]-1][bombPos[1]-1] = Label(startFrame, image=grassicon)
		labels[bombPos[0]-1][bombPos[1]-1].image = grassicon
		labels[bombPos[0]-1][bombPos[1]-1].place(x=(bombPos[1]-1)*18,y=(bombPos[0]-1)*18)
		mapData[bombPos[0]-1][bombPos[1]-1] = 'g'

	if mapData[bombPos[0]-1][bombPos[1]] != "w" and mapData[bombPos[0]-1][bombPos[1]] != "m":
		labels[bombPos[0]-1][bombPos[1]] = Label(startFrame, image=grassicon)
		labels[bombPos[0]-1][bombPos[1]].image = grassicon
		labels[bombPos[0]-1][bombPos[1]].place(x=(bombPos[1])*18,y=(bombPos[0]-1)*18)
		mapData[bombPos[0]-1][bombPos[1]] = 'g'

	if mapData[bombPos[0]-1][bombPos[1]+1] != "w" and mapData[bombPos[0]-1][bombPos[1]+1] != "m":
		labels[bombPos[0]-1][bombPos[1]+1] = Label(startFrame, image=grassicon)
		labels[bombPos[0]-1][bombPos[1]+1].image = grassicon
		labels[bombPos[0]-1][bombPos[1]+1].place(x=(bombPos[1]+1)*18,y=(bombPos[0]-1)*18)
		mapData[bombPos[0]-1][bombPos[1]+1] = 'g'

	if mapData[bombPos[0]][bombPos[1]-1] != "w" and mapData[bombPos[0]][bombPos[1]-1] != "m":
		labels[bombPos[0]][bombPos[1]-1] = Label(startFrame, image=grassicon)
		labels[bombPos[0]][bombPos[1]-1].image = grassicon
		labels[bombPos[0]][bombPos[1]-1].place(x=(bombPos[1]-1)*18,y=(bombPos[0])*18)
		mapData[bombPos[0]][bombPos[1]-1] = 'g'

	if mapData[bombPos[0]][bombPos[1]+1] != "w" and mapData[bombPos[0]][bombPos[1]+1] != "m":
		labels[bombPos[0]][bombPos[1]+1] = Label(startFrame, image=grassicon)
		labels[bombPos[0]][bombPos[1]+1].image = grassicon
		labels[bombPos[0]][bombPos[1]+1].place(x=(bombPos[1]+1)*18,y=(bombPos[0])*18)
		mapData[bombPos[0]][bombPos[1]+1] = 'g'

	if mapData[bombPos[0]+1][bombPos[1]-1] != "w" and mapData[bombPos[0]+1][bombPos[1]-1] != "m":
		labels[bombPos[0]+1][bombPos[1]-1] = Label(startFrame, image=grassicon)
		labels[bombPos[0]+1][bombPos[1]-1].image = grassicon
		labels[bombPos[0]+1][bombPos[1]-1].place(x=(bombPos[1]-1)*18,y=(bombPos[0]+1)*18)
		mapData[bombPos[0]+1][bombPos[1]-1] = 'g'

	if mapData[bombPos[0]+1][bombPos[1]] != "w" and mapData[bombPos[0]+1][bombPos[1]] != "m":
		labels[bombPos[0]+1][bombPos[1]] = Label(startFrame, image=grassicon)
		labels[bombPos[0]+1][bombPos[1]].image = grassicon
		labels[bombPos[0]+1][bombPos[1]].place(x=(bombPos[1])*18,y=(bombPos[0]+1)*18)
		mapData[bombPos[0]+1][bombPos[1]] = 'g'

	if mapData[bombPos[0]+1][bombPos[1]+1] != "w" and mapData[bombPos[0]+1][bombPos[1]+1] != "m":
		labels[bombPos[0]+1][bombPos[1]+1] = Label(startFrame, image=grassicon)
		labels[bombPos[0]+1][bombPos[1]+1].image = grassicon
		labels[bombPos[0]+1][bombPos[1]+1].place(x=(bombPos[1]+1)*18,y=(bombPos[0]+1)*18)
		mapData[bombPos[0]+1][bombPos[1]+1] = 'g'

	startFrame.pack(side=LEFT)

def howToPlay():
	homeFrame.pack_forget()
	
	howFrame = Frame(window, width = 25)
	photo = PhotoImage(file="./images/howtoplay-bg.png")
	picLbl = Label(howFrame, image=photo,width=600,height=505)
	picLbl.place(x=1, y=1, relwidth=1, relheight=1)
	backBtn = Button(picLbl, text = "Back", command = lambda: returnMenu(howFrame), bg = "silver", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	picLbl.pack()
	backBtn.pack()
	backBtn.place(x=60,y=18,anchor=CENTER)
	
	howFrame.pack()
	window.mainloop()

def highscores():
	homeFrame.pack_forget()
	
	hsFrame = Frame(window, width = 25)
	photo = PhotoImage(file="./images/highscore-bg.png")
	picLbl = Label(hsFrame, image=photo,width=600,height=505)
	picLbl.place(x=1, y=1, relwidth=1, relheight=1)
	backBtn = Button(picLbl, text = "Back", command = lambda: returnMenu(hsFrame), bg = "silver", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
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

'''============================================================================'''

window = Tk()
window.title("Bomberman")
window.geometry("600x505")
window.configure(background = "white")
'''===================================Game Menu================================'''
homeFrame = Frame(window, width = 600, height = 505)
#Background picture
photo = PhotoImage(file="./images/background.png")
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
window.mainloop()
'''============================================================================'''
