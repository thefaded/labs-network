import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ss.bind(('', 8899))
print("Ready! localhost:8899")

while 1:
    msg, cle = ss.recvfrom(2048)
    msg = msg.decode("utf-8") 
    msg += "----> Got your msg!"
    ss.sendto(str.encode(msg), cle)