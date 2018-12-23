import socket
import sys

def get_hex(num):
    return num[2:]

def task1(num):
    default_num = num
    num = int(num, 16)
    hexi = num.to_bytes(4, sys.byteorder)
    str = ''
    for byte in hexi:
        str += hex(byte) + ':'
    print('host byte order:')
    print('s_addr=' + default_num + ', ' + str[:-1])
    
def task2(num):
    default_num = num
    num = int(num, 16)
    res = hex(socket.htonl(num))
    default_num = res
    hexi = res[2:]
    if len(hexi) % 2 != 0:
        hexi = '0' + hexi   
    arr4 = bytearray.fromhex(hexi)
    str = ''
    for b in arr4[::-1]:
        str += hex(b) + ':'
    print('network byte order:')
    print('s_addr=' + default_num + ', ' + str[:-1])

def task3(num):
    res = bytearray.fromhex(get_hex(num))
    print('=' + socket.inet_ntop(socket.AF_INET, res))

def main():
    if (len(sys.argv) != 2):
        print('usage: python3 num in hexidecimal')
        sys.exit(0)
    num = sys.argv[1]
    task1(num)
    task2(num)
    task3(num)

main()