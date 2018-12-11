import socket
import sys
import select
import time
import queue
import tkinter as tk
import sys



from threading import Thread
from tcp_packet_pb2 import TcpPacket
from player_pb2 import Player

HOST = '202.92.144.45'
PORT = 80

server_address = (HOST, PORT)
#INSTANTIATE A SOCKET
socket = socket.socket()
#CONNECT TO SERVER
socket.connect(server_address)
#! /usr/bin/env python
#  -*- coding: utf-8 -*- platform: Darwin

def enterclicked(event):
	sendbtn()
def sendbtn():
	global player,connectPacket, packet
	chatPacket = packet.ChatPacket()
	socket.send(chat_packet_conf(player,packet,connectPacket.lobby_id,chatPacket))
	
			
def make_player(player_name):
	player = Player()
	player.name = player_name
	return player

def make_lobby(packet):
	#packet.type = CREATE_LOBBY from TcpPacket, 2. FROM TCP_PACKET.PY
	lobbyPacket = packet.CreateLobbyPacket()
	lobbyPacket.type = TcpPacket.CREATE_LOBBY
	maxNumPlayers = int(input("Enter max number of players: "))
	lobbyPacket.max_players = maxNumPlayers
	
	#SEND TO SERVER
	socket.send(lobbyPacket.SerializeToString()) 
	
	#RECEIVE FROM SERVER
	data = bytearray(socket.recv(1024))
	lobbyPacket.ParseFromString(data)
	print('Received from server: ' + lobbyPacket.lobby_id)
	lobby_id = lobbyPacket.lobby_id

	return lobby_id

def connect_packet_conf(connectPacket,player,packet,choice):
	connectPacket.type = TcpPacket.CONNECT
	if choice == 1:
		lobby_id = make_lobby(packet)
	else:
		lobby_id = input("Enter lobby id: ") 
	connectPacket.lobby_id = lobby_id
	connectPacket.player.name = player.name

	return connectPacket.SerializeToString()

def connect_player_to_server(player, packet):
	connectPacket = packet.ConnectPacket()

	choice = int(input("[1] Create a Lobby \n[2] Connect to Lobby \nEnter choice: "))

	if choice == 1:
		#SEND CONNECT PACKET TO SERVER
		socket.send(connect_packet_conf(connectPacket,player,packet,choice)) 

		#RECEIVE FROM SERVER
		connect_data = bytearray(socket.recv(1024))
		connectPacket.ParseFromString(connect_data)
	else:
		connectPacket.type = TcpPacket.ERR_LDNE
		while connectPacket.type == TcpPacket.ERR_LDNE or connectPacket.type == TcpPacket.ERR_LFULL:
			try:
				#SEND CONNECT PACKET TO SERVER
				socket.send(connect_packet_conf(connectPacket,player,packet,choice)) 
				
				#RECEIVE FROM SERVER
				connect_data = bytearray(socket.recv(1024))
				connectPacket.ParseFromString(connect_data)

				if connectPacket.type == TcpPacket.ERR_LFULL:
					print("Lobby is FULL.\n")
			except:
				if connectPacket.type == TcpPacket.ERR_LDNE:
					print("Lobby DOES NOT EXIST. Try entering another lobby id.\n")
	print('Received from server: ' + str(connectPacket))
	return connectPacket

def chat_packet_conf(player,packet, lobby_id,chatPacket):
	global top
	chatPacket.type = TcpPacket.CHAT
	chatPacket.message = top.msgTextBox.get("1.0",tk.END)
	chatPacket.player.name = player_name
	chatPacket.lobby_id = lobby_id

	return chatPacket.SerializeToString()


def chat_main():
	global top,player, packet, lobby_id, connectPacket
	packet_type = 0
	while True:
		list_of_sockets = [sys.stdin, socket] 

		#FOR CHAT PACKET 
		chatPacket = packet.ChatPacket()

		#FOR DISCONNECT CHAT PACKET
		disconnectPacket = packet.DisconnectPacket()
		disconnectPacket.type = TcpPacket.DISCONNECT

		read_sockets,write_socket,error_socket = select.select(list_of_sockets,[],[])

		for socks in read_sockets: 
			if socks == socket: 
				packet_received = bytearray(socket.recv(2048))
				packet.ParseFromString(packet_received)
				packet_type = packet.type 
				
				
				# 3: CHAT
				if packet_type == 3:
					#Receive broadcasted data from server
					chatPacket.ParseFromString(packet_received)
					top.msgTextBox.delete("1.0", tk.END)
					top.displayTextBox.configure(state="normal")
					top.displayTextBox.insert(tk.END,chatPacket.player.name+": "+chatPacket.message)
					top.displayTextBox.configure(state="disabled")
					print(chatPacket.player.name+": "+ chatPacket.message)

				# 1: CONNECT
				if packet_type == 1:
					connectPacket.ParseFromString(packet_received)
					top.displayTextBox.configure(state="normal")
					top.displayTextBox.insert(tk.END,connectPacket.player.name+" connected!\n")
					top.displayTextBox.configure(state="disabled")
					print(connectPacket.player.name + " connected!")

				# 0: DISCONNECT
				if packet_type == 0: 
					disconnectPacket.ParseFromString(packet_received)
					if disconnectPacket.player.name == "":
						if disconnectPacket.update == 0:
							top.displayTextBox.configure(state="normal")
							top.displayTextBox.insert("You left!")
							top.displayTextBox.configure(state="disabled")
							print("You left!")
						else:
							top.displayTextBox.configure(state="normal")
							top.displayTextBox.insert("Unknown error occured.\nYou have been disconnected from the game\n")
							top.displayTextBox.configure(state="disabled")
							print("Unknown error occured.\nYou have been disconnected from the game")
						sys.exit()
					else :	
						top.displayTextBox.configure(state="normal")
						top.displayTextBox.insert(tk.END,disconnectPacket.player.name+" left!\n")
						top.displayTextBox.configure(state="disabled")
						print(disconnectPacket.player.name + " left!")
			#MESSAGE
			else: 
				#SEND TO SERVER
				
				if chatPacket.message.strip() == "bye" or chatPacket.message.strip() == "exit":
					disconnectPacket.type = TcpPacket.DISCONNECT

					disconnectPacket.player.name = player_name
					socket.send(disconnectPacket.SerializeToString())


packet = TcpPacket()
player_name = input("Enter name: ")
player = make_player(player_name)

'''
GUI
'''
top = tk.Tk()
color = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85' 
_ana2color = '#ececec' # Closest X11 color: 'gray92' 

top.geometry("388x433+461+125")
top.title("Chat")
top.configure(background="#d9d9d9")
top.chatFrame = tk.Frame(top)
top.chatFrame.place(relx=0.0, rely=0.0, relheight=0.982, relwidth=0.992)

top.chatFrame.configure(relief='groove')
top.chatFrame.configure(borderwidth="2")
top.chatFrame.configure(relief='groove')
top.chatFrame.configure(background="#d9d9d9")
top.chatFrame.configure(width=385)



top.msgTextBox = tk.Text(top.chatFrame)
top.msgTextBox.place(relx=0.026, rely=0.8, relheight=0.193, relwidth=0.774)
top.msgTextBox.configure(background="white")
top.msgTextBox.configure(font="TkTextFont")
top.msgTextBox.configure(foreground="black")
top.msgTextBox.configure(highlightbackground="#d9d9d9")
top.msgTextBox.configure(highlightcolor="black")
top.msgTextBox.configure(insertbackground="black")
top.msgTextBox.configure(selectbackground="#c4c4c4")
top.msgTextBox.configure(selectforeground="black")
top.msgTextBox.configure(width=298)
top.msgTextBox.configure(wrap='word')
top.msgTextBox.bind("<Return>", enterclicked)


top.sendButton = tk.Button(top.chatFrame)
top.sendButton.place(relx=0.805, rely=0.871, height=22, width=71)
top.sendButton.configure(activebackground="#ececec")
top.sendButton.configure(activeforeground="#000000")
top.sendButton.configure(background="#d9d9d9")

top.sendButton.configure(foreground="#000000")
top.sendButton.configure(highlightbackground="#d9d9d9")
top.sendButton.configure(highlightcolor="black")
top.sendButton.configure(text='''Send''')
top.sendButton.configure(width=71)


top.displayTextBox = tk.Text(top.chatFrame)
top.displayTextBox.place(relx=0.0, rely=0.024, relheight=0.758, relwidth=0.982)
top.displayTextBox.configure(background="#000000")
top.displayTextBox.configure(font="TkTextFont")
top.displayTextBox.configure(foreground="#ffffff")
top.displayTextBox.configure(highlightbackground="#d9d9d9")
top.displayTextBox.configure(highlightcolor="black")
top.displayTextBox.configure(insertbackground="black")
top.displayTextBox.configure(selectbackground="#c4c4c4")
top.displayTextBox.configure(selectforeground="black")
top.displayTextBox.configure(state='disabled')
top.displayTextBox.configure(width=378)
top.displayTextBox.configure(wrap='word')

top.sendButton.configure(command=sendbtn)


connectPacket = connect_player_to_server(player, packet)
chatThread = Thread(target=chat_main)
chatThread.start()
top.mainloop()
socket.close() 