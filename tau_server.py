import socket

HOST = "chupacabra"
PORT = 6283

s = socket.socket(socket.AF_INET.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

conn, addr = s.accept()

print ("Connected by: ", addr)

while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)

conn.close()
