# TeleFXAutoForwarder (Telegram)

A Python-based automation script that **detects and forwards trading signals** (e.g. XAUUSD, GBPJPY, BTCUSD Buy/Sell signals) from one Telegram group/channel to another, with support for multiple trading instruments.

---

## 🚀 Setup Instructions

### ✅ 1. Install Dependencies

Make sure you have Python installed. Then open a terminal (CMD) and run:

```bash
pip install telethon colorama
```

---

### ✅ 2. Configure Your Credentials

Create a file named `info.json` in the same directory with the following format:

```json
{
  "api_id": YOUR_API_ID,
  "api_hash": "YOUR_API_HASH",
  "session_name": "forwarder_session",
  "routing": [
    {
      "source_chat_ids": [-1001234567890],
      "target_chat_ids": [-1009876543210]
    }
  ]
}
```

- Get your API ID and hash here: [Telegram API](https://my.telegram.org/auth?to=apps)
- Get group or channel chat IDs using:
  - [@getidsbot](https://t.me/getidsbot)
  - or this tool: [TeleChatIDs](https://github.com/hazyx7/TeleChatIDs)

---

## ▶️ How to Run

Run the script from your terminal:

```bash
python run.py
```

- On first run, enter your **phone number** to log in (or **bot token** if using a bot).
- Once logged in, the script will monitor and auto-forward matching signals.

---

## 📬 Signal Detection Criteria

Only messages containing **all of the following** will be forwarded:

- ✅ A clear **Buy** or **Sell**
- ✅ A defined **Stop Loss (SL)**
- ✅ At least one **Take Profit (TP)**

---

## 📊 Supported Symbols

The bot automatically detects and standardizes the following assets (case-insensitive):

- **Gold / XAUUSD**
- **Forex pairs:** GBPJPY, GBPUSD, EURUSD, USDJPY, AUDUSD, NZDUSD, etc.
- **Crypto:** BTCUSD, ETHUSD, etc.

> You can easily extend the list in the `SYMBOLS` dictionary inside the code.

---

### ✅ Examples that WILL be forwarded:

```
buy gold now @ 2322 - 2319
sl: 2316
tp1: 2327
tp2: 2332
```

```
sell GBPJPY @ 186.20 - 186.50
stop loss 186.80
tp1 185.90
tp2 185.50
```

```
buy btcusd @ 63000 - 63200
sl: 62750
tp: 63700
```

---

### ❌ Examples that will be skipped:

```
who's buying gold?
price alert: XAUUSD near 2325
```

```
SL/TP not mentioned
```

---

## 👨‍💻 Developer

Made with ❤️ by [@hazyx7](https://t.me/hazyx7)
