import json
import asyncio
import logging
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from colorama import init, Fore, Style
import re
import os

# === Initialize Colorama ===
init(autoreset=True)

# === Load Config ===
CONFIG_FILE = "info.json"
if not os.path.exists(CONFIG_FILE):
    print(Fore.RED + "Missing 'info.json'. Please create one.")
    input("Press Enter to exit...")
    exit()

with open(CONFIG_FILE, "r") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]
session_name = config.get("session_name", "forwarder_session")
routing = config["routing"]

# === Logging Setup ===
logging.basicConfig(
    level=logging.INFO,
    filename="bot_log.txt",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === Telegram Client ===
client = TelegramClient(session_name, api_id, api_hash)

# === Signal Extractor ===
def extract_valid_signal(text):
    lines = text.splitlines()
    cleaned = []
    tp_count = 1
    found_buy_sell = False
    found_tp = False

    for line in lines:
        line = line.strip()

        if not line or "money management" in line.lower():
            continue

        # Buy/Sell detection
        if re.search(r'\b(buy|sell)\b.*?(gold|xauusd)?', line, re.IGNORECASE):
            line = re.sub(r'gold', 'XAUUSD', line, flags=re.IGNORECASE)
            cleaned.append(line)
            cleaned.append("")  # Blank line
            found_buy_sell = True

        elif re.search(r'\d+\s*@\s*\d+(\.\d+)?\s*-\s*\d+(\.\d+)?', line):
            cleaned.append(line)

        # Stop Loss
        elif re.search(r'\bsl\b|stop loss', line, re.IGNORECASE):
            sl_match = re.search(r'(\d+(\.\d+)?)', line)
            if sl_match:
                cleaned.append(f"Stop Loss: {sl_match.group(1)}")
                cleaned.append("")  # Blank line

        # Take Profits
        elif 'tp' in line.lower():
            tps = re.findall(r'tp\d*\s*[:\-]?\s*(\d+(\.\d+)?)', line, re.IGNORECASE)
            for tp in tps:
                cleaned.append(f"Take Profit {tp_count}: {tp[0]}")
                tp_count += 1
                found_tp = True

    if found_buy_sell and found_tp:
        return '\n'.join(cleaned)
    return None

# === Logging Functions ===
async def log_skip(client, source_id):
    try:
        source_entity = await client.get_entity(source_id)
        source_title = getattr(source_entity, 'title', str(source_id))
        logging.info(f"Message skipped (no valid signal) — From: {source_title}")
    except:
        logging.info(f"Message skipped from {source_id}")

async def log_error(client, source_id, target_id, error):
    try:
        source_entity = await client.get_entity(source_id)
        target_entity = await client.get_entity(target_id)
        logging.error(
            f"Error forwarding from '{source_entity.title}' to '{target_entity.title}': {str(error)}"
        )
    except:
        logging.error(f"Error forwarding from {source_id} to {target_id}: {str(error)}")

# === Telegram Event Handler ===
@client.on(events.NewMessage())
async def handler(event):
    source_id = event.chat_id
    message_text = event.raw_text
    signal = extract_valid_signal(message_text)

    if signal:
        for route in routing:
            if source_id in route["source_chat_ids"]:
                for target in route["target_chat_ids"]:
                    try:
                        await client.send_message(target, signal)
                        # Get group names for display
                        source_entity = await client.get_entity(source_id)
                        target_entity = await client.get_entity(target)
                        source_name = getattr(source_entity, 'title', str(source_id))
                        target_name = getattr(target_entity, 'title', str(target))

                        print(Fore.GREEN + f"[✓] Forwarded from '{source_name}' to '{target_name}'")
                    except Exception as e:
                        await log_error(client, source_id, target, e)
                        print(Fore.RED + f"[✗] Failed to forward: {e}")
    else:
        await log_skip(client, source_id)
        print(Fore.YELLOW + f"[~] Skipped message from {source_id}")

# === Main Runner ===
async def main():
    print(Fore.CYAN + "\n📡 Logging into Telegram...")
    await client.start()
    me = await client.get_me()
    print(Fore.GREEN + f"✅ Logged in as {me.first_name} (@{me.username or me.id})")
    print(Fore.MAGENTA + "\n🚀 Signal Forwarder Running...\n" + Style.RESET_ALL)
    await client.run_until_disconnected()

# === Launch ===
try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    print(Fore.RED + "\n✋ Exiting... Goodbye!")
except Exception as e:
    print(Fore.RED + f"\n[ERROR] {e}")
    logging.error(f"Startup failed: {e}")
    input("Press any key to exit...")
