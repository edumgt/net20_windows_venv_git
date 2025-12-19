"""
03) URL 구조 이해: scheme/host/port/path/query
"""
from __future__ import annotations
import argparse
from urllib.parse import urlparse, parse_qs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="https://example.com:443/path?a=1&b=2")
    args = ap.parse_args()

    u = urlparse(args.url)
    print("url:", args.url)
    print(" scheme:", u.scheme)
    print(" host:", u.hostname)
    print(" port:", u.port)
    print(" path:", u.path)
    print(" query:", u.query)
    print(" query parsed:", parse_qs(u.query))

if __name__ == "__main__":
    main()
