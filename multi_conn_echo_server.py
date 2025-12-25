import socket

def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 12345))
    s.listen()
    s.setblocking(False)
    connections = []

    try:
        while True:
            try:
                conn, client_addr = s.accept()
                print(f"A connection has been established with {client_addr}")
                conn.setblocking(False)
                connections.append((conn, client_addr))
            except BlockingIOError:
                pass

            for conn, client_addr in connections[:]:
                try:
                    data = conn.recv(1024)
                except BlockingIOError:
                    continue

                if not data:
                    continue

                print(f"recv from {client_addr}: {data}")
                conn.send(b"echo: " + data)


                if data == b'bye\r\n':
                    print(f"connection with {client_addr} closed")
                    conn.close()
                    connections.remove((conn, client_addr))

    except KeyboardInterrupt:
            s.close()

if __name__ == "__main__":
        run_server()

