#!/usr/bin/env python3
import sys
import socket
import selectors

sel = selectors.DefaultSelector()

def accept(sock, mask):
  conn, addr = sock.accept()
  print("connection from", addr)
  conn.setblocking(False)
  sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
  data = conn.recv(2 ** 10)
  if data:
    print("from", conn, data.decode(), end='')
    conn.send(data)
  else:
    print("closing", conn.getpeername())
    sel.unregister(conn)
    conn.close()

def main():
  if len(sys.argv) != 2:
    print("usage:", sys.argv[0], "<sock-port>")
    sys.exit(0)

  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_ip = '127.0.0.1'
    s_port = int(sys.argv[1])
    sock.bind((s_ip, s_port))

    possible_connections = 2

    sock.listen(possible_connections)
    sock.setblocking(False)

    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
      events = sel.select()
      for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
    
  except OSError as e:
    print("OSError:", e)
  except socket.gaierror as e:
    print(e)

main()