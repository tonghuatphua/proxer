import socket

HOST = '0.0.0.0'
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024)
            if request:
                response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nPONG"
                conn.sendall(response)
