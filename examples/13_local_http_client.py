"""
13) 로컬 HTTP 서버 호출(클라이언트)
- 예) python 12_local_http_server.py 를 먼저 켜고 실행
"""
from __future__ import annotations
import argparse, requests

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="http://127.0.0.1:8001")
    args = ap.parse_args()

    print("GET /health ->", requests.get(args.base + "/health", timeout=2).json())
    print("GET /hello?name=kim ->", requests.get(args.base + "/hello", params={"name":"kim"}, timeout=2).json())

if __name__ == "__main__":
    main()
