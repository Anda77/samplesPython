import socket

def scan(ip, port):
    try:
        sock= socket.socket()
        sock.connect(ip, port)
        print("port opened " + str(port))
        sock.close()
    except:
        print("port closed " + str(port))


scan("89.42.221.60", 80)