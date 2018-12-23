# import sys
# import socket

# def task1(domain):
#     print('1.4: getaddrinfo, IPv4')
#     res = socket.getaddrinfo(domain, 80, socket.AF_INET, socket.SOCK_STREAM, 0, 0)
#     for a in res:
#         print(a[4][0])

# def task2(domain):
#     print('1.5: getaddrinfo, IPv4 + IPv6')
#     res = socket.getaddrinfo(domain, 80, 0, socket.SOCK_STREAM, 0, 0)
#     for a in res:
#         print(a[4][0])

# def task3(domain, port):
#     print('1.6: getaddrinfo, IPv4, IPv6, номер порта')
#     print('For ' + domain + ' with ' + port)
#     res = socket.getaddrinfo(domain, port, 0, socket.SOCK_STREAM, 0, 0)
#     for a in res:
#          print(socket.getnameinfo(a[4], socket.SOCK_RAW)[0] + ' with port ' + socket.getnameinfo(a[4], socket.SOCK_RAW)[1])

# def main():
#     if (len(sys.argv) != 3):
#         print('usage: python3 + domain + domain-service')
#         sys.exit(0)
#     domain = sys.argv[1]
#     port = sys.argv[2]

#     task1(domain)
#     task2(domain)
#     task3(domain, port)
# main()

import sys
import socket

def task1(domain):
    res = socket.getaddrinfo(domain, '80', 0, 0, socket.IPPROTO_TCP)

    for a in res:
        print(a)

def main():
    domain = sys.argv[1]
    port = sys.argv[2]
    task1(domain)

main()