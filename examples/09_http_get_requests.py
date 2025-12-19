"""
09) requests로 HTTP GET (더 쉬운 라이브러리)
"""
from __future__ import annotations
import argparse, requests

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="https://example.com")
    args = ap.parse_args()

    r = requests.get(args.url, timeout=3, headers={"User-Agent": "Net20-requests"})
    print("status:", r.status_code)
    print("content-type:", r.headers.get("content-type", ""))
    print("body sample:", r.text[:200].replace("\n", " "))

if __name__ == "__main__":
    main()
