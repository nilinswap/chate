#server.py
import socket
class Server:
	def __init__(self, ip = ''):
		'''
			stores name to ip map in dic.
		'''
		self.adr = ip
		self.port = 7777
		self.map = {}
		self.cli_listen_port = 8888

	def run(self):
		'''
			A method whose task is to keep listening to clients asking for IP for a particular connection.
			It also registers a name with IP. so message can be of two types. register or reply.
		'''
		self.sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind(('', self.port))

		while True:
			msg, addr = self.sock.recvfrom(1024)
			msg = msg.decode()
			lis = msg.split(' ')
			if lis[0] == 'register':
				name = lis[1]
				ip = addr[0]
				#this is the part where I make entry
				self.map[name] = ip
				print(self.map)
				# INCREASE RELIABLITY HERE
			elif lis[0] == 'close':
				name = lis[1]
				ip = addr[0]
				#this is the part where I remove entry
				del(self.map[name])
				print(self.map)
				# INCREASE RELIABLITY HERE		
			elif lis[0] == 'reply':
				name = lis[1]
				new_msg = self.map[name]
				new_msg = 'reply ' + new_msg
				new_msg = new_msg.encode();
				adr_tup = addr[0], self.cli_listen_port
				sendto(new_msg, adr_tup)


def cli_test():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('', 8888))
	adr_tup = '172.20.51.18', 7777
	msg = 'register B'
	msg = msg.encode()
	sock.sendto(msg, adr_tup)

	msg = 'reply B'
	msg = msg.encode()
	sock.sendto(msg, adr_tup)
	new_msg, addr = sock.recvfrom(1024)
	print(new_msg, addr)
if __name__ == '__main__':
	test()
