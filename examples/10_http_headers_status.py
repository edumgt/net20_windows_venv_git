"""
10) 상태코드/헤더/인코딩 살펴보기
"""
from __future__ import annotations
import requests

def main():
    url = "https://example.com"
    r = requests.get(url, timeout=3)

    print("URL:", url)
    print("status:", r.status_code)
    print("encoding:", r.encoding)
    print("headers (top 6):")
    for k in list(r.headers.keys())[:6]:
        print(" ", k, ":", r.headers[k])

if __name__ == "__main__":
    main()
