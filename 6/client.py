import socket
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = "Client message. TCP Test!"

while 1:
    clientSocket.send(str.encode(message))
    data = clientSocket.recv(1024)
    print(data)