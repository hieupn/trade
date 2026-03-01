from flask import Flask, request, jsonify
import requests as req

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def ticker(path):
    symbol = request.args.get("symbol", "BTCUSDT").upper()
    try:
        r = req.get(
            "https://api.binance.com/api/v3/ticker/24hr",
            params={"symbol": symbol},
            timeout=8
        )
        resp = jsonify(r.json())
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Cache-Control"] = "no-cache"
        return resp, 200
    except Exception as e:
        resp = jsonify({"error": str(e)})
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp, 500
