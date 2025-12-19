"""
15) TCP 에코 서버(소켓 서버)
- 클라이언트가 보낸 문자열을 그대로 돌려줌
- 터미널 1에서 실행
"""
from __future__ import annotations
import socket, threading

HOST = "127.0.0.1"
PORT = 9001

def handle(conn: socket.socket, addr):
    print("client connected:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(b"ECHO: " + data)
    print("client closed:", addr)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"TCP Echo Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()
