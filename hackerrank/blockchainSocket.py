#!/usr/bin/python
import socket

server = 'ws.blockchain.info'
port = 80 # websocket
server_address = (server, port)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print  'starting up on %s port %s' % server_address
sock.connect(server_address)
print 'Connected'

subscribe_message = b'{"op":"ping"}'
sock.sendall(subscribe_message)
data = sock.recv(1024)
print data
sock.close()
print 'Exiting sucessfully'