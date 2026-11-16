# Main python file
import socket


HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.bind((HOST, PORT))
    f.listen(1)

    conn = f.accept()
    addr = f.accept()

    with conn:
        print("Connected by: ", addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)