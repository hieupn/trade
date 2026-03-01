const https = require("https");

function fetchURL(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => resolve(data));
    }).on("error", reject);
  });
}

module.exports = async (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, OPTIONS");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Content-Type", "application/json");

  if (req.method === "OPTIONS") {
    res.status(204).end();
    return;
  }

  const { action = "ticker", symbol = "BTCUSDT", interval = "5m", limit = "200" } = req.query;
  const sym = symbol.toUpperCase();

  try {
    if (action === "ticker") {
      const data = await fetchURL(
        `https://api.binance.com/api/v3/ticker/24hr?symbol=${sym}`
      );
      res.status(200).send(data);

    } else if (action === "klines") {
      const data = await fetchURL(
        `https://api.binance.com/api/v3/klines?symbol=${sym}&interval=${interval}&limit=${limit}`
      );
      const raw = JSON.parse(data);
      const candles = raw.map((k) => ({
        t: k[0],
        o: parseFloat(k[1]),
        h: parseFloat(k[2]),
        l: parseFloat(k[3]),
        c: parseFloat(k[4]),
        v: parseFloat(k[5]),
      }));
      res.status(200).json(candles);

    } else {
      res.status(400).json({ error: "unknown action" });
    }
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
};
