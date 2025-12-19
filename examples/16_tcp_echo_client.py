"""
16) TCP 에코 클라이언트
- 터미널 2에서 실행(서버 먼저 실행)
"""
from __future__ import annotations
import argparse, socket

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=9001)
    ap.add_argument("--msg", default="hello")
    args = ap.parse_args()

    with socket.create_connection((args.host, args.port), timeout=3) as s:
        s.sendall(args.msg.encode("utf-8"))
        data = s.recv(1024)
        print("received:", data.decode("utf-8", errors="replace"))

if __name__ == "__main__":
    main()
