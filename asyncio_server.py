import asyncio
import socket

async def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 12345))
    s.listen()
    s.setblocking(False)

    loop = asyncio.get_event_loop()

    try:
        while True:
            conn, client_addr = await loop.sock_accept(s)
            print(f"connection established with {client_addr}")

            while data := await loop.sock_recv(conn, 1024):
                msg = b'echo: '
                msg += data
                await loop.sock_sendall(conn, msg)


                if data == b'bye\r\n':
                    conn.close()
                    print(f"connection with {client_addr} closed")
                    break

    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    asyncio.run(run_server())
