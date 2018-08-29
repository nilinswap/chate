#listen_side_tcp_connect.py
import os
import sys
import socket

def func():
	serv_sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	port = 6666
	serv_sock.bind(("", port)) 
	cli_adr =  sys.argv[1], port
	serv_sock.listen(5)
	#cli_sock.connect(serv_adr)
	cli_sock = serv_sock.accept()

	while True:
		in_st = input()
		msg =in_st.encode()
		cli_sock.send(msg)
		st = cli_sock.recv(1024).decode()
		print("\t\t st");

if __name__ == '__main__':
	func()