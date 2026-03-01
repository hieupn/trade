from flask import Flask, request, jsonify
import requests as req

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def klines(path):
    symbol   = request.args.get("symbol",   "BTCUSDT").upper()
    interval = request.args.get("interval", "5m")
    limit    = request.args.get("limit",    "200")
    try:
        r = req.get(
            "https://api.binance.com/api/v3/klines",
            params={"symbol": symbol, "interval": interval, "limit": limit},
            timeout=10
        )
        raw = r.json()
        candles = [
            {
                "time":   k[0],
                "open":   float(k[1]),
                "high":   float(k[2]),
                "low":    float(k[3]),
                "close":  float(k[4]),
                "volume": float(k[5])
            }
            for k in raw
        ]
        resp = jsonify(candles)
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Cache-Control"] = "no-cache"
        return resp, 200
    except Exception as e:
        resp = jsonify({"error": str(e)})
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp, 500
