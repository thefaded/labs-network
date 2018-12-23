#!/usr/bin/python
import socket, select, sys

host = '127.0.0.1'
port = 8898

READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
READ_WRITE = READ_ONLY | select.POLLOUT
TIMEOUT = 1000

if len(sys.argv) != 2:
    print("usage:", sys.argv[0], "<sock-port>")
    sys.exit(0)

port = int(sys.argv[1])

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    # sock.setblocking(0)
    sock.listen(5)
    # Ready to get inputs
    inputs = [sock]
    outputs = []
    ml = {}

    poller = select.poll()
    poller.register(server, READ_ONLY)

    while 1:
        events = poller.poll(TIMEOUT)
        
        for fd, flag in events:
            s = fd_to_socket[fd]

            if flag & (select.POLLIN | select.POLLPRI):
                if s is server:
                # A "readable" server socket is ready to accept a connection
                connection, client_address = s.accept()
                print >>sys.stderr, 'new connection from', client_address
                connection.setblocking(0)
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                # Give the connection a queue for data we want to send
                message_queues[connection] = Queue.Queue()
            else:
                data = s.recv(1024)

                 if data:
                    # A readable client socket has data
                    print >>sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
                    message_queues[s].put(data)
                    # Add output channel for response
                    poller.modify(s, READ_WRITE)
            elif flag & select.POLLOUT:

except OSError as e:
    print("OSError:", e)
except socket.gaierror as e:
    print(e)