"""
18) 재시도(backoff) 기본
- 네트워크는 가끔 "잠깐" 실패합니다. 그럴 때 재시도가 유용합니다.
"""
from __future__ import annotations
import requests
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

@retry(stop=stop_after_attempt(4), wait=wait_exponential_jitter(initial=0.3, max=2.0), reraise=True)
def get_with_retry(url: str) -> int:
    r = requests.get(url, timeout=2)
    return r.status_code

def main():
    url = "https://httpbin.org/status/200"
    code = get_with_retry(url)
    print("status:", code)

if __name__ == "__main__":
    main()
