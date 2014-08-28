# (C) Ululab, all rights reserved

import socket

def get_ipaddress():
	return socket.gethostbyname(socket.gethostname())
	
if __name__ == '__main__':
	print(get_ipaddress())