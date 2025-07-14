<h1 align="center">📶 HCO-WifiSnag</h1>
<p align="center"><b>Fake Wi-Fi Login Page to Snag Passwords (For Testing & Educational Use Only)</b></p>

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

## 🧠 About

**HCO-WifiSnag** is a realistic Wi-Fi login simulator tool used to demonstrate how social engineering tactics can be used to collect sensitive data like Wi-Fi passwords — made for **educational awareness**, **pentesting demos**, and **ethical testing**.

It creates a professional-looking fake Wi-Fi reconnect page that tricks users into entering their password while locking all interaction except input.

---

## 🛠️ Features

- ✅ Looks like a real "Wi-Fi Disconnected" prompt  
- ✅ Freezes page until password is entered  
- ✅ Blocks inspect, copy, or dev tools  
- ✅ Spinner + fake reconnection animation  
- ✅ Captures password in Termux live  
- ✅ Built-in YouTube subscription check  
- ✅ Lightweight Flask-based interface

---

## ⚙️ Full Termux Setup (From Scratch)

### 🔁 1. Install Termux Packages

```bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install flask
pkg install cloudflared -y
```

### 📥 2. Clone the Tool

```bash
git clone https://github.com/Hackerscolonyofficial/HCO-WifiSnag.git
cd HCO-WifiSnag
```

### 🔐 3. Start the Tool

```bash
chmod +x start.sh
./start.sh
```

👉 You will be redirected to Hackers Colony YouTube channel  
👉 After subscribing, return and press **Enter** to continue

---

## ☁️ Cloudflared Tunnel Setup

Open **another Termux tab**, and run:

```bash
cloudflared tunnel --url http://127.0.0.1:8080
```

✅ You’ll get a public link like:
```
https://something.trycloudflare.com
```

💬 Send that link to your victim/test user.  
🛑 When they enter their Wi-Fi password, it will show in Termux.

---

## 📦 Requirements

- Python 3  
- Flask (`pip install flask`)  
- Termux  
- Cloudflared (`pkg install cloudflared`)

Optional:
```bash
pip install -r requirements.txt
```

---

## ⚠️ Disclaimer

> This tool is made strictly for **educational purposes**, awareness demos, and legal penetration testing.  
> Do not use it without clear, written permission.  
> The developer is **not responsible for any misuse**.

---

## 💬 Hacker Quote

> “The quieter you become, the more you are able to hear.” — Anonymous

---

## 👨‍💻 Code by Azhar  
🔗 Project by **Hackers Colony**
