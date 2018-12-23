import socket
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((serverName, serverPort))

MESSAGE = input("tcpClientA: Enter message, or EXIT to quit")

while MESSAGE != 'exit':
    tcpClientA.send(str.encode(MESSAGE))
    data = tcpClientA.recv(1024)
    print("tcpClientA received data:", data)
    MESSAGE = input("tcpClientA: Enter message, or EXIT to quit")