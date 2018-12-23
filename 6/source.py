import sys
import socket

def main():
    if len(sys.argv) != 2:
        print("usage:", sys.argv[0], "PORT")
        sys.exit(0)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_ip = '127.0.0.1'
        sock_port = int(sys.argv[1])
        sock.bind((sock_ip, sock_port))
        sock.listen(1)

        print("Ready to receive messages on: ", (sock_ip, sock_port))

        while 1:
            connectionSocket, addr = sock.accept()
            data = connectionSocket.recv(1024)
            print("Getting data from socket...", data)
            print("Peername: ", connectionSocket.getpeername())
            print("Nameinfo: ", socket.getnameinfo(addr, 0))
            connectionSocket.sendall(data)

        sock.close()
    except OSError as e:
        print("OSError:", e)
    except socket.gaierror as e:
        print(e)

main()