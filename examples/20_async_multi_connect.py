"""
20) asyncio로 여러 대상 동시에 접속(맛보기)
- 동시성의 장점: 여러 서버를 순차로 기다리지 않고 동시에 처리 가능
"""
from __future__ import annotations
import asyncio, argparse

async def tcp_ping(host: str, port: int, timeout: float) -> dict:
    try:
        fut = asyncio.open_connection(host, port)
        reader, writer = await asyncio.wait_for(fut, timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return {"host": host, "port": port, "ok": True}
    except Exception as e:
        return {"host": host, "port": port, "ok": False, "error": str(e)}

async def main_async(host: str, ports: list[int], timeout: float):
    tasks = [tcp_ping(host, p, timeout) for p in ports]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(r)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="example.com")
    ap.add_argument("--ports", default="80,443,8080")
    ap.add_argument("--timeout", type=float, default=1.2)
    args = ap.parse_args()
    ports = [int(x.strip()) for x in args.ports.split(",") if x.strip()]
    asyncio.run(main_async(args.host, ports, args.timeout))

if __name__ == "__main__":
    main()
