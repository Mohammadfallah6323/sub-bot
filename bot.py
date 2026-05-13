import requests
import re

BOT_TOKEN = "8790547965:AAFQdVlNhgKwHsUIWMEA0o4YBzC0OBl0UCY"
CHAT_ID = "-1003766000771"
SUB_LINK = "لینک_ساب_تو_اینجا_بذار"

def get_usage():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(SUB_LINK, headers=headers)
    info = r.headers.get("subscription-userinfo")
    if not info:
        return "❌ اطلاعات حجم پیدا نشد"

    upload = re.search(r'upload=(\d+)', info)
    download = re.search(r'download=(\d+)', info)
    total = re.search(r'total=(\d+)', info)

    used = int(upload.group(1)) + int(download.group(1))
    total_bytes = int(total.group(1))
    remain = total_bytes - used

    gb = 1024**3
    used_gb = round(used / gb, 2)
    remain_gb = round(remain / gb, 2)
    total_gb = round(total_bytes / gb, 2)

    return f"""
📊 وضعیت اشتراک

🔹 حجم کل: {total_gb} GB
🔹 مصرف شده: {used_gb} GB
🔹 باقی‌مانده: {remain_gb} GB
"""

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

if name == "main":
    msg = get_usage()
    send_message(msg)
