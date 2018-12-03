'''
!!! Click anywhere on the map first before pressing keys
Controls
w: up
a: left
s: down
d: right
'''

from tkinter import *
from PIL import Image, ImageTk

def key(event):
	action(event.char)

def callback(event):
    startFrame.focus_set()

def action(move):
	global mapData
	global playerPos
	global startFrame
	global labels
	tempLabel = Label(startFrame)

	if move == 'd': 	#right
		if mapData[playerPos[0]][playerPos[1]+1] == 'g':
			tempLabel = labels[playerPos[0]][playerPos[1]]
			labels[playerPos[0]][playerPos[1]] = labels[playerPos[0]][playerPos[1]+1]
			labels[playerPos[0]][playerPos[1]+1] = tempLabel
			labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1])*18,y=playerPos[0]*18)
			labels[playerPos[0]][playerPos[1]+1].place(x=(playerPos[1]+1)*18,y=playerPos[0]*18)

			startFrame.pack()

			mapData[playerPos[0]][playerPos[1]+1] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[1] = playerPos[1] + 1
	elif move == 'a': 	#left
		if mapData[playerPos[0]][playerPos[1]-1] == 'g':
			tempLabel = labels[playerPos[0]][playerPos[1]]
			labels[playerPos[0]][playerPos[1]] = labels[playerPos[0]][playerPos[1]-1]
			labels[playerPos[0]][playerPos[1]-1] = tempLabel
			labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1])*18,y=playerPos[0]*18)
			labels[playerPos[0]][playerPos[1]-1].place(x=(playerPos[1]-1)*18,y=playerPos[0]*18)

			startFrame.pack()

			mapData[playerPos[0]][playerPos[1]-1] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[1] = playerPos[1] - 1
	elif move == 'w': 	#up
		if mapData[playerPos[0]-1][playerPos[1]] == 'g':
			tempLabel = labels[playerPos[0]][playerPos[1]]
			labels[playerPos[0]][playerPos[1]] = labels[playerPos[0]-1][playerPos[1]]
			labels[playerPos[0]-1][playerPos[1]] = tempLabel
			labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1])*18,y=playerPos[0]*18)
			labels[playerPos[0]-1][playerPos[1]].place(x=(playerPos[1])*18,y=(playerPos[0]-1)*18)

			startFrame.pack()

			mapData[playerPos[0]-1][playerPos[1]] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[0] = playerPos[0] - 1
	elif move == 's': 	#down
		if mapData[playerPos[0]+1][playerPos[1]] == 'g':
			tempLabel = labels[playerPos[0]][playerPos[1]]
			labels[playerPos[0]][playerPos[1]] = labels[playerPos[0]+1][playerPos[1]]
			labels[playerPos[0]+1][playerPos[1]] = tempLabel
			labels[playerPos[0]][playerPos[1]].place(x=(playerPos[1]*18),y=playerPos[0]*18)
			labels[playerPos[0]+1][playerPos[1]].place(x=(playerPos[1]*18),y=(playerPos[0]+1)*18)

			startFrame.pack()

			mapData[playerPos[0]+1][playerPos[1]] = 'p'
			mapData[playerPos[0]][playerPos[1]] = 'g'
			playerPos[0] = playerPos[0] + 1
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
				player = Image.open("./images/player.png")
				playericon = ImageTk.PhotoImage(player)
				labels[i][j] = Label(startFrame, image=playericon)
				labels[i][j].image = playericon
				labels[i][j].place(x=ypos,y=xpos)
			ypos = ypos + 18
		xpos = xpos + 18
	startFrame.bind("<Key>", key)
	startFrame.bind("<Button-1>", callback)
	startFrame.pack()

def start(): 
	global mapData
	global startFrame
	global playerPos
	global backBtn

	homeFrame.pack_forget()
	window.geometry("800x505")
	startFrame = Frame(window,width = 600, height = 505)
	
	backBtn = Button(window, text = "Back", command = lambda: returnMenu(startFrame), bg = "silver", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	
	backBtn.place(x=60,y=18,anchor=CENTER)
	backBtn.pack()
	
	mapData = loadFileReader() #reads the map file and writes to a 2d array
	playerPos = {}
	playerPos[0] = 1 #x position
	playerPos[1] = 1 #y position

	initMap()
	window.mainloop()
	

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
