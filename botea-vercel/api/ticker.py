import requests
from http.server import BaseHTTPRequestHandler
import json

BINANCE = "https://api.binance.com/api/v3"

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Parse symbol from query string
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        symbol = params.get("symbol", ["BTCUSDT"])[0].upper()

        try:
            r = requests.get(f"{BINANCE}/ticker/24hr", params={"symbol": symbol}, timeout=8)
            data = r.json()
            body = json.dumps(data).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(body)

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, format, *args):
        pass
