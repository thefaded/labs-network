# Lab 3
#
# Copyright (c) 2018 Daniil Pankratev
#
# This code is licensed under a MIT-style license.

import sys
import socket

def task1(ip, port):
    hosts = socket.getaddrinfo(ip, port, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
    for host in hosts:
        print(host[4])
    return hosts[0]

def task2(first_host):
    host_family = first_host[0]
    host_type = first_host[1]
    host_proto = first_host[2]

    soc = socket.socket(family=host_family, type=host_type, proto=host_proto)
    print("New socket created: ", soc)
    return soc

def task3(soc, ip, port):
    soc.connect((ip, int(port)))
    print("Connected succs")

def task4(soc):
    message = str.encode("GET / HTTP/1.0\nHost: ya.ru\n\n")
    print("message size:", soc.send(message))

def task5(soc):
    print("\ntask_5:")
    ans = ""
    while True:
        data = soc.recv(2 ** 10)
        if not data:
            break
        ans += data.decode()
    print(ans)

def task6(soc):
    print("\ntask_6:")
    print(soc.getsockname())

def main():
    if len(sys.argv) != 3:
        print("usage:", sys.argv[0], "iPv4 service")
        sys.exit(0)
    
    ip = sys.argv[1]
    port = sys.argv[2]

    try:
        first_host = task1(ip, port)
        soc = task2(first_host)
        task3(soc, ip, port)
        task4(soc)
        task5(soc)
        task6(soc)
    except OSError as e:
        print("OSError: ", e)
    except socket.gaierror as e:
        print(e)

main()
