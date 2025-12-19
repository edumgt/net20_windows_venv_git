"""
17) UDP 한 번 보내보기(연결 없는 통신)
- UDP는 "보냈다"가 곧 "도착했다"는 뜻이 아님(확인 응답이 없으면 모름)
- 여기서는 같은 PC에서 send/recv를 같이 실행
"""
from __future__ import annotations
import socket, threading, time

HOST = "127.0.0.1"
PORT = 9002

def receiver():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        s.settimeout(5)
        data, addr = s.recvfrom(2048)
        print("recv from", addr, ":", data.decode("utf-8", errors="replace"))

def sender():
    time.sleep(0.3)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"hello udp", (HOST, PORT))
        print("sent to", (HOST, PORT))

def main():
    t1 = threading.Thread(target=receiver, daemon=True)
    t1.start()
    sender()
    t1.join(timeout=6)

if __name__ == "__main__":
    main()
