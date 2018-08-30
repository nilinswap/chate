#server.py
import socket
class Server:
	port = 7777
	cli_service_port = 8888
	def __init__(self, ip = ''):
		'''
			stores name to ip map in dic.
		'''
		self.ip = ip
		self.map = {}
		self.port_pool = set([])
		

	def run(self):
		'''
			A method whose task is to keep listening to clients asking for IP for a particular connection.
			It also registers a name with IP. so message can be of two types. register or reply.
		'''
		self.sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind(('', self.port)) #binds this process('s socket) to the port. See Ip binding is not possible because are you faking??.

		while True:
			msg, addr = self.sock.recvfrom(1024)
			msg = msg.decode()
			lis = msg.split(' ')
			if lis[0] == 'register': # e.g. register new_name
				name = lis[1]
				ip = addr[0]
				#this is the part where I make entry
				self.map[name] = ip
				print(self.map)
				# INCREASE RELIABLITY HERE
			elif lis[0] == 'close':  # e.g. close name
				name = lis[1]
				ip = addr[0]
				#this is the part where I remove entry
				del(self.map[name])
				print(self.map)
				# INCREASE RELIABLITY HERE		
			elif lis[0] == 'request': # e.g. request name
				name = lis[1]
				try:
					ip = self.map[name]
					new_msg = 'reply ' + ip
				except KeyError as e:
					print(" KeyError for ", name)
					new_msg = 'error ' + e
				finally:
					new_msg = new_msg.encode();
					adr_tup = addr[0], self.cli_service_port
					self.sock.sendto(new_msg, adr_tup)
			else:
				print("else")
				pass


def test():
	server = Server()
	server.run()
def cli_test():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('', 8888))
	adr_tup = '172.20.51.18', 7777
	msg = 'register B'
	msg = msg.encode()
	sock.sendto(msg, adr_tup)

	msg = 'request B'
	msg = msg.encode()
	sock.sendto(msg, adr_tup)
	new_msg, addr = sock.recvfrom(1024)
	print(new_msg, addr)
if __name__ == '__main__':
	test()
