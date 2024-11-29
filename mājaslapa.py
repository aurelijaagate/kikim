from flask import Flask, render_template_string, jsonify
import random
import os

app = Flask(__name__)

# HTML kods kā Flask veidne
HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Do you love me?</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        .container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #e94d58;
            font-size: 24px;
            margin-bottom: 15px;
        }
        img {
            width: 300px;
            border-radius: 10px;
        }
        .buttons {
            margin-top: 20px;
        }
        button {
            padding: 10px 20px;
            font-size: 18px;
            margin: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .yes-btn {
            background: #e94d58;
            color: white;
        }
        .no-btn {
            background: white;
            color: #e94d58;
            border: 2px solid #e94d58;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Do you love me?</h2>
        <img id="gif" src="https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif" alt="Cute gif">
        <div class="buttons">
            <button class="yes-btn" onclick="showLove()">Yes</button>
            <button class="no-btn" onclick="moveButton(this)">No</button>
        </div>
    </div>
    <script>
        function showLove() {
            document.querySelector('h2').innerText = "You got Rickrolled 😘";
            document.querySelector('#gif').src = "https://media.giphy.com/media/Vuw9m5wXviFIQ/giphy.gif";
        }
        function moveButton(button) {
            const container = document.querySelector('.container');
            const rect = container.getBoundingClientRect();
            const randomX = Math.random() * (rect.width - button.offsetWidth);
            const randomY = Math.random() * (rect.height - button.offsetHeight);
            button.style.position = 'absolute';
            button.style.left = `${randomX}px`;
            button.style.top = `${randomY}px`;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    # Izmanto "os.environ.get('PORT')" dinamiskai porta piešķiršanai Render platformā
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
