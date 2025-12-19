"""
19) 간단 모니터링: 주기적으로 체크하고 로그 남기기
- '상태코드'와 '응답시간'만 기록해도 운영에 도움 됨
"""
from __future__ import annotations
import argparse, time, requests
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="https://example.com")
    ap.add_argument("--interval", type=float, default=2.0)
    ap.add_argument("--count", type=int, default=3)
    args = ap.parse_args()

    logp = Path("reports/monitor.log")
    logp.parent.mkdir(parents=True, exist_ok=True)

    for i in range(args.count):
        t0 = time.time()
        try:
            r = requests.get(args.url, timeout=3)
            ms = int((time.time()-t0)*1000)
            line = f"{time.strftime('%H:%M:%S')} ok status={r.status_code} ms={ms} url={args.url}"
        except Exception as e:
            ms = int((time.time()-t0)*1000)
            line = f"{time.strftime('%H:%M:%S')} fail ms={ms} url={args.url} err={e}"

        print(line)
        logp.write_text((logp.read_text(encoding="utf-8") if logp.exists() else "") + line + "\n", encoding="utf-8")
        time.sleep(args.interval)

    print("log saved:", logp.resolve())

if __name__ == "__main__":
    main()
