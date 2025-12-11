import socket

def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 12345))

    s.listen()

    try:
    # accept a connection from a client
    # when a connection is created ephemeral port is bound to the connetion socket

        connection, client_addr = s.accept()
        print(f"connection established with {client_addr}")

         # use client_socket to communicate with the client
        data = connection.recv(1024)
        print(f"data is working with {data}")

        # close the client socket when its done
        connection.close()
    except KeyboardInterrupt:
        s.close()


if __name__ == "__main__":
    run_server()


