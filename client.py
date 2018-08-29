import socket
import os
import sys
import threading
serv_adr_tup = ('172.20.51.18', 7777)
def get_ip(sock, name):
	'''
		gets ip from name. contacts server for that.
	'''
	msg = 'request '+name 
	msg = msg.encode()
	sock.sendto(msg, serv_adr_tup)
	new_msg, addr = sock.recvfrom(1024) #It is not yet discrimination to the server
	new_msg = new_msg.decode()
	lis = new_msg.split(' ')
	if lis[0] == 'reply':
		ip = lis[1]
		return ip
	else:
		print('else')
		return 'else'

"""
def get_name(sock, ip):
	'''
		gets name from ip. contacts server for that.
	'''
	msg = 'request '+ ip 
	msg = msg.encode()
	sock.sendto(msg, serv_adr_tup)
	new_msg, addr = sock.recvfrom(1024) #It is not yet discrimination to the server
	new_msg = new_msg.decode()
	lis = new_msg.split(' ')
	if lis[0] == 'reply':
		ip = lis[1]
		return ip
	else:
		print('else')
		return 'else'
"""

def inform_other_ok(listener_sock, ip):
	'''
		informs that there is a socket here ready to accept connection from other side.
		Other side is running service.py.
	'''
	msg = 'OK'
	msg = msg.encode()
	adr_tup = ip, 8888
	listener_sock.sendto( msg, adr_tup)




def listener():
	'''
		it is run in a seperate thread and its task is to listen to incoming request for connection
		and create a listener tcp connection in a new screen.
	'''
	listener_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	listener_sock.bind(('', 9999))
	while True:
		msg, addr = listener_sock.recvfrom(1024)
		msg = msg.decode()
		lis = msg.split(' ')
		other_peer_ip = addr[0]
		if lis[0] == 'connect': # e.g. connect other_persons_name
			other_peer_name = lis[1]
			tcp_listen_command = 'python3 listen_side_tcp_connect.py ' + other_peer_ip
			os.system("screen -S "+ other_peer_name + " -d -m " + tcp_listen_command )
			inform_ok(listener_sock, other_peer_ip)


		elif msg == 'close':
			print('close')
		else:
			print('else')
def register_name(service_sock, cli_name):
	'''
		registers client's name with its ip in server
	'''
	msg = 'register '+cli_name 
	msg = msg.encode()
	service_sock.sendto(msg, serv_adr_tup)
	
def service():
	service_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	service_sock.bind(('', 8888))
	your_name = sys.argv[1]
	register_name(service_sock, your_name)
	while True:
		in_st = input().rstrip().lstrip()
		lis = in_st.split(' ')
		command = lis[0]
		if command == 'connect': # e.g. connect other_persons_name
			other_peer_name = lis[1]
			other_peer_ip = get_ip(service_sock, other_peer_name)
			tcp_service_command = 'python3 service_side_tcp_connect.py ' + other_peer_ip
			os.system("screen -S "+ other_peer_name + " -d -m " + tcp_listen_command )
			#inform_ok(listener_sock, other_peer_ip)
			print("\t connection established. please move to screen.")


		elif command == 'close':
			print('close')
		else:
			print('else')