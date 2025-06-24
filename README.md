# TeleFXAutoForwarder (Telegram)

This is a Python-based Telegram bot that automatically **detects and forwards trading signals** (such as "XAUUSD Buy/Sell signals") from one group/channel to another.

---

## ⚙️ Features

- ✅ Filters and forwards only **valid trading signals**
- ✅ Skips unrelated messages (e.g. "who buys gold now?")
- ✅ Replaces group/channel IDs with human-readable names in logs
- ✅ Clean formatting with color logs and error handling
- ✅ Configurable routing: multiple source → multiple target groups

---

## 🧰 Requirements

- Python 3.8 or above
- A Telegram account
- A Telegram API ID and API hash (from [my.telegram.org](https://my.telegram.org))

---

## 🚀 Setup Instructions

### -> Install dependencies
```bash
pip install telethon colorama
```

### -> Configure your credentials

Place/ Put ur informations in the `info.json` in the same directory.
You can get chat IDs using Telegram bots like [@getidsbot](https://t.me/getidsbot).

---

## ▶️ How to Run

```bash
python run.py
```

- On the first run, enter your phone number (or bot token).
- Once authenticated, the bot will start forwarding signals automatically.

---

## 📬 Signal Detection Format

Only messages containing:

- ✅ A **Buy** or **Sell** keyword
- ✅ A **Stop Loss** (SL)
- ✅ At least one **Take Profit** (TP)

…will be forwarded.

### ✅ Examples that WILL be forwarded:

```
gold buy now @ 3322 - 3319
sl : 3316
tp1 : 3327
tp2 : 3332
```

```
sell xauusd @ 3345 - 3347
sl 3350
tp 3335
tp 3320
```

### ❌ Examples that will be skipped:

```
who buy gold now?
xauusd current price: 3328
```

---

## 📝 Logs

- Logs are saved to `bot_log.txt`
- Skipped messages and all forwardings are timestamped and labeled clearly

---

## 🧑‍💻 Creator

Made by [@hazyx777](https://t.me/hazyx777)
