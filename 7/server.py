#  while true ; do nc -z 127.0.0.1 8899 ; done;

import socket
import sys
from _thread import start_new_thread

HOST = '127.0.0.1'

def client_socket_thread(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

def main():
    if len(sys.argv) != 2:
        print("usage:", sys.argv[0], "PORT")
        sys.exit(0)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = int(sys.argv[1])
        s.bind((HOST, port))
        s.listen(5)

        while True:
            conn, addr = s.accept()
            print("Connected to " + addr[0] + ":" + str(addr[1]))
            # Thread
            start_new_thread(client_socket_thread, (conn,))
        s.close()

    except OSError as e:
        print("OSError:", e)
    except socket.gaierror as e:
        print(e)
main()