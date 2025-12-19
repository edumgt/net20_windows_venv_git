"""
02) 내 PC의 호스트 이름/로컬 IP 확인
- 로컬 IP는 공유기/회사망 내부에서 쓰는 주소일 수 있음
"""
from __future__ import annotations
import socket

def main():
    hostname = socket.gethostname()
    print("hostname:", hostname)

    try:
        local_ip = socket.gethostbyname(hostname)
        print("local ip:", local_ip)
    except Exception as e:
        print("failed to get local ip:", e)

if __name__ == "__main__":
    main()
