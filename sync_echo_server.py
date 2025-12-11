import socket

def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 12345))

    s.listen()

    try:
        while True:
            connection, client_addr = s.accept()
            print(f"connection established with {client_addr}")

            # use client_socket to communicate with the client
            while True:
                data = connection.recv(1024)
                print(data)
                msg = b'echo: '
                msg += data
                connection.send(msg)

                if data == b'bye\r\n':
                    connection.close()
                    break
    except KeyboardInterrupt:
        s.close()






if __name__ == "__main__":
    run_server()




