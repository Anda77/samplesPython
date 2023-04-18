import socket


def scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        print(result)
        if result == 0:
            print("port opened: " + str(port))
            sock.close()
    except:
        print("port closed: " + str(port))


scan("89.42.221.60", 21)

scan("89.42.221.60", 80)

scan("85.204.108.49", 21)

scan("85.204.108.49", 80)

# scan("http://www1.pythonprograming.net/", 80)
