# Binance Futures Testnet Trading Bot

A CLI-based trading bot for the Binance Futures Testnet (USDT-M). Built in Python, it lets you place market, limit, and stop-limit orders directly from the terminal — with an optional Streamlit UI if you prefer a browser interface.

---

## Features

- Place **Market**, **Limit**, and **Stop-Limit** orders
- Supports both **BUY** and **SELL** sides
- Input validation before any order is sent
- Logs all API requests, responses, and errors
- Clean modular structure — easy to read and extend
- Optional **Streamlit UI** (`ui/app.py`)

---

## Project Structure

```
trading-bot/
├── bot/
│   ├── cli.py          # Command-line interface
│   ├── client.py       # Binance API client
│   ├── orders.py       # Order placement logic
│   ├── validators.py   # Input validation
│   ├── config.py       # API keys and settings
│   ├── logger.py       # Logging setup
│   └── exceptions.py   # Custom exceptions
├── ui/
│   └── app.py          # Streamlit UI (optional)
├── logs/               # Log files stored here
├── requirements.txt
└── README.md
```

---

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/your-username/trading-bot.git
cd trading-bot
```

**2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your API keys**

Open `bot/config.py` and fill in your Binance Futures Testnet credentials:

```python
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_api_secret"
```

> Get your testnet keys at: https://testnet.binancefuture.com

---

## How to Run

**CLI mode**

```bash
python -m bot.cli
```

**Streamlit UI**

```bash
streamlit run ui/app.py
```

---

## Example Inputs

**Market Order**

```
Symbol:     BTCUSDT
Side:       BUY
Order Type: MARKET
Quantity:   0.001
```

**Limit Order**

```
Symbol:     BTCUSDT
Side:       SELL
Order Type: LIMIT
Quantity:   0.001
Price:      65000
```

**Stop-Limit Order**

```
Symbol:      BTCUSDT
Side:        BUY
Order Type:  STOP_LIMIT
Quantity:    0.001
Price:       67000
Stop Price:  66500
```

---

## Logs

All logs are saved in the `logs/` directory. Each session logs:

- Outgoing API requests
- Responses from Binance
- Any errors or validation failures

---

## Notes

- This bot runs on the **Testnet only** — no real funds are used.
- Make sure your testnet account has enough balance before placing orders.
- Minimum quantity for BTCUSDT is `0.001` — going lower will throw a validation error.
- Do not use production API keys with this project.


## Author

Shivraj Patil