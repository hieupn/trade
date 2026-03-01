import requests
from http.server import BaseHTTPRequestHandler
import json

BINANCE = "https://api.binance.com/api/v3"

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        symbol   = params.get("symbol",   ["BTCUSDT"])[0].upper()
        interval = params.get("interval", ["5m"])[0]
        limit    = params.get("limit",    ["200"])[0]

        try:
            r = requests.get(
                f"{BINANCE}/klines",
                params={"symbol": symbol, "interval": interval, "limit": limit},
                timeout=10
            )
            data = r.json()

            # Convert to clean OHLCV objects
            candles = [
                {
                    "time":   k[0],
                    "open":   float(k[1]),
                    "high":   float(k[2]),
                    "low":    float(k[3]),
                    "close":  float(k[4]),
                    "volume": float(k[5])
                }
                for k in data
            ]

            body = json.dumps(candles).encode()
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
