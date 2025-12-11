import selectors
import socket

def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 12345))
    s.listen()
    s.setblocking(False)

    selector = selectors.DefaultSelector()
    selector.register(s, selectors.EVENT_READ)

    try:
        while True:
            events = selector.select(timeout=1)

            if len(events) == 0:
                continue

            for event, _ in events:
                event_socket = event.fileobj

                if event_socket == s:
                    conn, client_addr = s.accept()
                    print(f"connection established with {client_addr}")
                    selector.register(conn, selectors.EVENT_READ)
                else:
                    conn = event_socket
                    data = conn.recv(1024)
                    msg = b'echo: '
                    msg += data
                    conn.send(msg)

                    if data == b'bye\r\n':
                        conn.close()
                        print(f"connection with {client_addr} closed")
                        break

    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    run_server()


