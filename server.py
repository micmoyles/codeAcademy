#!/usr/bin/python 

import socket
port = 9876
print 'opening ', str(port)
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))

s.listen(5)

c, addr = s.accept()
print 'Got connection from ', addr
c.send( 'Hello' )
