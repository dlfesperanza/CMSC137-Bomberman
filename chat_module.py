import socket
import sys
import select
from tcp_packet_pb2 import TcpPacket
from player_pb2 import Player

HOST = '202.92.144.45'
PORT = 80

server_address = (HOST, PORT)
#INSTANTIATE A SOCKET
socket = socket.socket()
#CONNECT TO SERVER
socket.connect(server_address)

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
		connect_data = bytearray(socket.recv(1024)) # receive response from server
		connectPacket.ParseFromString(connect_data)
	else:
		connectPacket.type = TcpPacket.ERR_LDNE
		while connectPacket.type == TcpPacket.ERR_LDNE or connectPacket.type == TcpPacket.ERR_LFULL:
			try:
				#SEND CONNECT PACKET TO SERVER
				socket.send(connect_packet_conf(connectPacket,player,packet,choice)) 
				
				#RECEIVE FROM SERVER
				connect_data = bytearray(socket.recv(1024)) # receive response from server
				connectPacket.ParseFromString(connect_data)

				if connectPacket.type == TcpPacket.ERR_LFULL:
					print("Lobby is FULL.\n")
			except:
				if connectPacket.type == TcpPacket.ERR_LDNE:
					print("Lobby DOES NOT EXIST. Try entering another lobby id.\n")
	print('Received from server: ' + str(connectPacket))  # show in terminal
	return connectPacket

def chat_packet_conf(player,packet, lobby_id,chatPacket):
	chatPacket.type = TcpPacket.CHAT
	chatPacket.message = sys.stdin.readline()
	chatPacket.player.name = player_name
	chatPacket.lobby_id = lobby_id

	return chatPacket.SerializeToString()

def chat_main(player, packet, lobby_id, connectPacket):
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
					print(chatPacket.player.name+": "+ chatPacket.message)

				# 1: CONNECT
				if packet_type == 1:
					connectPacket.ParseFromString(packet_received)
					print(connectPacket.player.name + " connected!")

				# 0: DISCONNECT
				if packet_type == 0: 
					disconnectPacket.ParseFromString(packet_received)
					if disconnectPacket.player.name == "":
						#if the disconnection is normal
						if disconnectPacket.update == 0:
							print("You left!")
						else:
							print("Unknown error occured.\nYou have been disconnected from the game")
						sys.exit()
					else :
						print(disconnectPacket.player.name + " left!")
			#MESSAGE
			else: 
				#SEND TO SERVER
				socket.send(chat_packet_conf(player,packet,lobby_id,chatPacket))

				if chatPacket.message.strip() == "bye" or chatPacket.message.strip() == "exit":
					disconnectPacket.type = TcpPacket.DISCONNECT

					disconnectPacket.player.name = player_name
					socket.send(disconnectPacket.SerializeToString())


packet = TcpPacket()
player_name = input("Enter name: ")
player = make_player(player_name)
connectPacket = connect_player_to_server(player, packet)
chat_main(player, packet, connectPacket.lobby_id, connectPacket)
socket.close() 
