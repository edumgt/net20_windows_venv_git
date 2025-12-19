# Windows: 서버가 필요 없는 예제만 안전하게 실행
$ErrorActionPreference = "Stop"

python examples\01_what_is_ip_port.py --host example.com
python examples\02_my_ip_and_hostname.py
python examples\03_parse_url.py --url "https://example.com:443/path?a=1&b=2"
python examples\04_tcp_connect.py --host example.com --port 443
python examples\05_check_ports_allowlist.py --host example.com --ports "80,443"
python examples\07_read_banner.py --host example.com --port 80
python examples\08_http_get_urllib.py --url https://example.com
python examples\09_http_get_requests.py --url https://example.com
python examples\10_http_headers_status.py
python examples\11_http_json_api.py --name kim
python examples\14_download_file_stream.py --url https://example.com --out reports\download.html
python examples\18_retry_backoff_basic.py
python examples\19_simple_monitor_loop.py --url https://example.com --count 2 --interval 1
python examples\20_async_multi_connect.py --host example.com --ports "80,443"
