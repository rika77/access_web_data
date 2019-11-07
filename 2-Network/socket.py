# Socket -- connection between 2 computers

import socket
# Diale the phone
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # Host & Port