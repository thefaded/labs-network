# Lab2
#
# Copyright (c) 2018 Daniil Pankratev
#
# This code is licensed under a MIT-style license.

import sys
import socket

def beautify(bin_ip):
    str = ""
    for a in bin_ip:
        str += hex(a)
        str += ":"
    return str[:-1]

def task1(ip):
    bin_ip = socket.inet_pton(socket.AF_INET, ip)
    print(beautify(bin_ip), "\n")

def task2(ip):
    # Creating tuple
    sock_addr = (ip, 80)
    # Getting host/port by iP address
    host, port = socket.getnameinfo(sock_addr, 0)
    print("Domain: ", host, "\n")

def task3(ip, port):
    # Creating tuple
    sock_addr = (ip, int(port))
    # Getting host/port by iP address
    host, port = socket.getnameinfo(sock_addr, 0)
    print("Domain: ", host)
    print("Service: ", port)

def main():
    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        print("Usage: ", sys.argv[0], "iPv4 Port (optional)")
        sys.exit(0)
    
    ip = sys.argv[1]
    
    try:
        if len(sys.argv) >= 2:
            task1(ip)
            task2(ip)
        
        if len(sys.argv) >= 3:
            port = sys.argv[2]
            task3(ip, port)
    
    except OSError as e:
        print("OSError: ", e)
    except socket.gaierror as e:
        print("Socket error: ", e)

main()
