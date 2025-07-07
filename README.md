# TeleFXAutoForwarder (Telegram)

This is a Python-based automation that automatically **detects and forwards trading signals** (such as "XAUUSD Buy/Sell signals") from one group/channel to another.

---

## 🚀 Setup Instructions

### -> Install dependencies
```bash
pip install telethon colorama
```

### -> Configure your credentials

Put ur credentials in the `info.json` in the same directory.

get your api and hash here [Telegram API](https://my.telegram.org/auth?to=apps)

you can get chat IDs using Telegram bots like [@getidsbot](https://t.me/getidsbot)
OR
use this to get chat IDs [TeleChatIDs](https://github.com/hazyx7/TeleChatIDs)

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

## 🧑‍💻 Creator

Made by [@hazyx7](https://t.me/hazyx7)
