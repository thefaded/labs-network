#!/usr/bin/python
import socket, select, sys
import queue

host = '127.0.0.1'
port = 8898

if len(sys.argv) != 2:
    print("usage:", sys.argv[0], "<sock-port>")
    sys.exit(0)

port = int(sys.argv[1])

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    # Ready to get inputs
    inputs = [server]
    outputs = []
    message_queues = {}

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        # inputs
        for s in readable:
            if s is server:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                print("New connection from: ", client_address)
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    message_queues[s].put(data)

                    if s not in outputs:
                        outputs.append(s)
                    else:
                        if s in outputs:
                            outputs.remove(s)
                        inputs.remove(s)
                        s.close()
                        del message_queues[s]
        # outputs
        for s in writable:
            try:
                next_msg = message_queues[s].get_nowait()
            except Queue.Empty:
                 outputs.remove(s)
            else:
                 s.send(next_msg)

except OSError as e:
    print("OSError:", e)
except socket.gaierror as e:
    print(e)