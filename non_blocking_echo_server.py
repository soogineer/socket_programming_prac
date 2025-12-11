
import socket

def run_server():
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 12345))
    s.listen()

    s.setblocking(False)

    try:
        while True:
            try:
                connection, client_addr = s.accept()
                print(f"A connection has been established with {client_addr}")
            except BlockingIOError:
                continue

        while True:
            try:
                data = connection.recv(1024)
            except BlockingIOError:
                continue

            print(data)
            msg = b'echo: '
            msg += data
            connection.send(msg)

            if data == b'bye\r\n':
                connection.close()
                print(f"connection with {client_addr} closed")
                break

    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    run_server()
