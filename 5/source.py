# Lab 5
#
# Copyright (c) 2018 Daniil Pankratev
#
# This code is licensed under a MIT-style license.

import sys
import socket

# Task 5.1/5.2/5.3
def task1(port, back=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_ip = '127.0.0.1'
    sock_port = int(port)
    sock.bind((sock_ip, sock_port))

    print("Ready to listen (IP, PORT) = ", (sock_ip, sock_port))

    while 1:
        data, addr = sock.recvfrom(2 ** 10)
        
        if back:
            sock.sendto(data, addr)

        data = data.decode("utf-8")
        addr = socket.getnameinfo(addr, 0)
        print("(Host, Port) =", addr)
        print("Data =", data)
        break

# Task 5.4
def task2(sock_p, ipv4, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_ip = '127.0.0.1'
    sock_port = int(sock_p)
    sock.bind((sock_ip, sock_port))
    sock.connect((ipv4, port))

    while 1:
        data, addr = sock.recvfrom(2 ** 10)
        addr = socket.getnameinfo(addr, 0)

        print("(Host, Port) =", addr)
        print("Data =", data)


def main():
    if len(sys.argv) != 2 and len(sys.argv) != 4:
        print("usage:", sys.argv[0], "Socket_port Remote_iPv4 Remote_port")
        sys.exit(0)

    port = sys.argv[1]

    try:
        # Switch True/False
        if len(sys.argv) == 2:
            task1(port, True)
        if len(sys.argv) == 4:
            ipv4 = sys.argv[2]
            port_r = int(sys.argv[3])
            task2(port, ipv4, port_r)

    except OSError as e:
        print("OSError:", e)
    except socket.gaierror as e:
        print(e)

main()