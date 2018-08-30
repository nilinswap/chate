#service_side_tcp_connect.py
import os
import sys
import socket
import threading
rec_port = 6667
send_port = 6666

def receive_func():
	#print("hi everyone")
	cli_sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	port = rec_port
	cli_sock.bind(("", port)) 
	serv_adr =  sys.argv[1], port
	
	cli_sock.connect(serv_adr)
	while True:
		#in_st = input()
		
		#msg =in_st.encode()
		#cli_sock.send(msg)
		st = cli_sock.recv(1024).decode()
		print("\t\t ", st);
def send_func():
	#print("hi everyone")
	cli_sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	port = send_port
	cli_sock.bind(("", port)) 
	serv_adr =  sys.argv[1], port
	
	cli_sock.connect(serv_adr)
	while True:
		in_st = input()
		msg =in_st.encode()
		cli_sock.send(msg)
		#st = cli_sock.recv(1024).decode()
		#print("\t\t ", st);
def func():
	print("hi everyone!")
	'''thr1 = threading.Thread(target = receive_fun)
	thr2 = threading.Thread(target = send_fun)
	thr1.start()
	thr2.start()
	'''
	receive_fun()
if __name__ == '__main__':
	func()