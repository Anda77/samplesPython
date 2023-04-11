

import socket
import termcolor
import sys

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("ip address is: " + remoteServerIP)
def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect_ex((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except KeyboardInterrupt:
		print("You pressed Ctrl+C")
		sys.exit()

	except socket.gaierror:
		print("Hostname could not be resolved. Exiting")
		sys.exit()

	except socket.error:
		print("Couldn't connect to server")
		sys.exit()


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
