import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if data.decode().find("Hello") != -1:
            	conn.send('Hello, MODULE is here'.encode())
            elif data.decode().find("GET_TEMPERATURE") != -1:
            	conn.send('22.0'.encode())
            