from tkinter import *

def start(): #Displays How to Play in GUI
	homeFrame.pack_forget()
	window.geometry("800x505")
	startFrame = Frame(window,width = 800, height = 505)
	photo = PhotoImage(file="./images/start-bg.png")
	picLbl = Label(startFrame, image=photo,width=600,height=505)
	picLbl.place(x=1, y=1, relwidth=1, relheight=1)
	backBtn = Button(picLbl, text = "Back", command = lambda: returnMenu(startFrame), bg = "silver", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	
	# b=Button(picLbl,justify = LEFT)
	# photo=PhotoImage(file="./images/start-def.png")
	# b.config(image=photo,width="100",height="100")
	# b.pack(side=LEFT)

	picLbl.pack()
	backBtn.pack()
	backBtn.place(x=60,y=20,anchor=CENTER)

	
	
	startFrame.pack()
	window.mainloop()

def howToPlay(): #Displays How to Play in GUI
	homeFrame.pack_forget()
	
	howFrame = Frame(window, width = 25)
	photo = PhotoImage(file="./images/howtoplay-bg.png")
	picLbl = Label(howFrame, image=photo,width=600,height=505)
	picLbl.place(x=1, y=1, relwidth=1, relheight=1)
	backBtn = Button(picLbl, text = "Back", command = lambda: returnMenu(howFrame), bg = "silver", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	picLbl.pack()
	backBtn.pack()
	backBtn.place(x=60,y=20,anchor=CENTER)
	
	howFrame.pack()
	window.mainloop()

def highscores(): #Displays How to Play in GUI
	homeFrame.pack_forget()
	
	hsFrame = Frame(window, width = 25)
	photo = PhotoImage(file="./images/highscore-bg.png")
	picLbl = Label(hsFrame, image=photo,width=600,height=505)
	picLbl.place(x=1, y=1, relwidth=1, relheight=1)
	backBtn = Button(picLbl, text = "Back", command = lambda: returnMenu(hsFrame), bg = "silver", width = 8, fg = "black", font = ("Quicksand", 12),relief="groove") 
	picLbl.pack()
	backBtn.pack()
	backBtn.place(x=60,y=20,anchor=CENTER)
	
	hsFrame.pack()
	window.mainloop()

def exit(): #For Exit button; exits the GUI/game
	window.destroy()

def returnMenu(frame): #Forgets previous frame
	frame.pack_forget()
	homeFrame.pack()
	window.geometry("600x505")

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