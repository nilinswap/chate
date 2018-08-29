#service_side_tcp_connect.py
import os
import sys
import socket

def func():
	print("hi everyone")
	cli_sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	port = 6666
	cli_sock.bind(("", port)) 
	serv_adr =  sys.argv[1], port
	
	cli_sock.connect(serv_adr)
	while True:
		in_st = input()
		
		msg =in_st.encode()
		cli_sock.send(msg)
		st = cli_sock.recv(1024).decode()
		print("\t\t ", st);

if __name__ == '__main__':
	func()