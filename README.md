# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot to place orders on Binance Futures Testnet (USDT-M).

---

## Features

- Place MARKET, LIMIT, and STOP-LIMIT orders  
- Supports BUY and SELL  
- Input validation  
- Logs API requests and responses  
- Clean modular structure  

---

## Project Structure
trading-bot/
│
├── bot/
│   ├── cli.py           # CLI entry point
│   ├── client.py        # Binance client setup
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   ├── config.py        # Environment variables
│   ├── logger.py        # Logging setup
│   └── exceptions.py    # Custom exceptions
│
├── ui/
│   └── app.py           # Streamlit UI (optional)
│
├── logs/                # Log files
├── requirements.txt
└── README.md
---

## Setup

### 1. Clone repo
git clone https://github.com/theshivrajpatil/trading-bot.git
cd trading-bot
---

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
---

### 3. Install dependencies
pip install -r requirements.txt
---

### 4. Add API keys

Create `.env` file in root:
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret
BASE_URL=https://testnet.binancefuture.com
---

## Testnet Setup (IMPORTANT)

1. Go to: https://testnet.binancefuture.com  
2. Login (GitHub recommended)  
3. Add funds using **Faucet**  
4. Create API keys  
5. Use those keys in `.env`  

---

## Run
python bot/cli.py
---

## Example Runs

### MARKET Order
BTCUSDT
BUY
MARKET
0.001
yes
---

### LIMIT Order
BTCUSDT
SELL
LIMIT
0.001
80000
yes
---

### STOP-LIMIT Order
BTCUSDT
BUY
STOP_LIMIT
0.001
60000
61000
yes
---

## Logs

Logs are saved in:logs/bot.log
---

## Notes

- Works only on Binance Futures Testnet  
- Use small quantities (e.g., 0.001 BTC)  
- `.env` file is not included for security  

---

## Author

Shivraj Patil