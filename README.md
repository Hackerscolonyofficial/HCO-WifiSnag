<h1 align="center">📶 HCO-WifiSnag</h1>
<p align="center"><b>Fake Wi-Fi Login Page to Snag Passwords</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-Python-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Termux-informational?style=flat-square" />
  <img src="https://img.shields.io/badge/Tool-Type-Social_Engineering-critical?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Final-green?style=flat-square" />
</p>

<p align="center">
  <a href="https://www.instagram.com/hackers_colony_official"><img src="https://img.shields.io/badge/Instagram-Hackers--Colony-critical?style=flat-square&logo=instagram"></a>
  <a href="https://t.me/hackersColony"><img src="https://img.shields.io/badge/Telegram-Channel-blue?style=flat-square&logo=telegram"></a>
  <a href="https://www.facebook.com/share/1AY25it2Em/"><img src="https://img.shields.io/badge/Facebook-Page-blue?style=flat-square&logo=facebook"></a>
  <a href="https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"><img src="https://img.shields.io/badge/YouTube-Subscribe-red?style=flat-square&logo=youtube"></a>
</p>

---

## 💡 About

**HCO-WifiSnag** is a powerful ethical tool designed for **educational and testing** purposes. It simulates a Wi-Fi reconnect page in a realistic, frozen-like interface that tricks users into entering their Wi-Fi password — then displays it in your terminal.

---

## ⚙️ Features

- Fake Wi-Fi reconnect UI (100% realistic)
- Locks page to only allow password entry
- Spinner + connection failed if left empty
- Works on all phones and browsers
- Password shown live in Termux
- Lightweight and fast

---

## 📲 Termux Setup

```bash
pkg update && pkg install python git -y
pip install flask
pkg install cloudflared -y
git clone https://github.com/Hackerscolonyofficial/HCO-WifiSnag.git
cd HCO-WifiSnag
pip install -r requirements.txt
python main.py
```

➡️ Tool will auto-redirect you to our YouTube channel for subscription  
➡️ After subscribing, press **Enter** to continue

---

## ☁️ Cloudflared Link Setup

In **another Termux tab**, run:

```bash
cloudflared tunnel --url http://127.0.0.1:5000
```

You will get a `https://randomstring.trycloudflare.com` link  
📤 Send that link to your target — password will appear in Termux

---

## 📦 Requirements

- Python 3
- Flask
- Termux + cloudflared

You can install all with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Disclaimer

> This tool is **only for educational and authorized testing**.  
> Do not use against anyone without **clear permission**.  
> We are not responsible for any misuse.

---

## 💬 Hacker’s Motivation

> “The quieter you become, the more you are able to hear.” — Anonymous

---

## 👨‍💻 Code by Azhar  
🔗 Project by **Hackers Colony**
