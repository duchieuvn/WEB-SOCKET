import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 6543

# SOCKET INIT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((SERVER_IP, SERVER_PORT))
s.listen()


#-------------------------main---------------------
print("waiting for browser client")
conn,addr = s.accept()

print(addr, "connected")
msg = conn.recv(1024).decode()

print(msg)


# SERVER response to web browser
res = "HTTP/1.1 200 OK\r\n\r\n<h1>HELLO AE</h1>"

conn.sendall(res.encode())

conn.close()
s.close()

