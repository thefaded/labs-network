# Lab 4
#
# Copyright (c) 2018 Daniil Pankratev
#
# This code is licensed under a MIT-style license.

import sys
import socket

# Find addresses iPv4 and UDP
def task1(ip, port):
    hosts = socket.getaddrinfo(ip, port, family=socket.AF_INET, proto=socket.IPPROTO_UDP)
    for host in hosts:
        print(host[4])
    return hosts[0]

# Create socket for addr
def task2(addr):
    host_family = addr[0]
    host_type = addr[1]
    host_proto = addr[2]
    
    sock = socket.socket(family=host_family, type=host_type, proto=host_proto)
    print("New socket created!")
    return sock

# Send messages and receive
def task3(sock, addr):
    message = str.encode("Hehe!")

    sock.sendto(message, addr)
    data, address = sock.recvfrom(2 ** 10)
    print("Response: ", data, " From: ", address)

# Send with connect / send
def task4(sock, addr):
    message = str.encode("Hehe! With connect(), send()")
    
    sock.connect(addr)
    sock.send(message)
    
    data, address = sock.recvfrom(2 ** 10)
    print("Response: ", data, " From: ", address)

def task5(send_ip, send_port, remote_ip, remote_port):
    ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ss.bind((send_ip, send_port))
    message = str.encode("Hello from lab4!")

    ss.sendto(message, (remote_ip, remote_port))
    data, address = ss.recvfrom(2 ** 10)
    print("Response: ", data, " From: ", address)

def main():
    ip = sys.argv[1]
    port = int(sys.argv[2])

    rem_ip = sys.argv[3]
    rem_port = int(sys.argv[4])

    task5(ip, port, rem_ip, rem_port)
    # if len(sys.argv) != 4:
    #     print("usage:", sys.argv[0], "iPv4 Port")
    #     sys.exit(0)

    # ip = sys.argv[1]
    # port = sys.argv[2]

    # try:
    #     addr = task1(ip, port)
    #     sock = task2(addr)
    #     task3(sock, addr[4])
    #     task4(sock, addr[4])
    # except OSError as e:
    #     print("OSError:", e)
    # except socket.gaierror as e:
    #     print(e)

main()