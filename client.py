import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8000))

msg = s.recv(5)
print(msg.decode('utf-8'))
