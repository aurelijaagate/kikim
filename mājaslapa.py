from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Special Page for You</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: black;
            overflow: hidden;
            font-family: Arial, sans-serif;
            color: white;
        }
        .stars {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            background: black;
            overflow: hidden;
        }
        .stars div {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: moveStar 5s linear infinite;
        }
        @keyframes moveStar {
            from {transform: translateY(0);}
            to {transform: translateY(100vh);}
        }
        .wrapper {
            position: relative;
            width: 400px;
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            z-index: 2;
        }
        h2 {
            font-size: 2em;
            color: #4A90E2;
            text-shadow: 2px 2px 4px #888888;
        }
        .gif {
            width: 100%;
            max-width: 300px;
            margin: 15px 0;
            border-radius: 10px;
        }
        .btn-group {
            margin-top: 20px;
            position: relative;
            height: 40px;
        }
        button {
            width: 150px;
            height: 40px;
            color: white;
            font-size: 1.2em;
            border-radius: 30px;
            outline: none;
            cursor: pointer;
            box-shadow: 0 2px 4px gray;
            border: 2px solid #e94d58;
        }
        button.yes-btn {
            background: #e94d58;
        }
        button.no-btn {
            background: white;
            color: #e94d58;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
        }
        #particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div class="stars" id="stars"></div>
    <div class="wrapper">
        <h2 class="question">Do you love me?</h2>
        <img class="gif" alt="gif" src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" />
        <div class="btn-group">
            <button class="yes-btn">Yes</button>
            <button class="no-btn">No</button>
        </div>
    </div>
    <audio id="audio" src="" preload="auto"></audio>
    <script>
        const yesBtn = document.querySelector(".yes-btn");
        const noBtn = document.querySelector(".no-btn");
        const question = document.querySelector(".question");
        const gif = document.querySelector(".gif");
        const audio = document.getElementById("audio");
        const body = document.body;

        const questions = [
            "Do you think I'm funny?",
            "Would you like to watch a movie together?",
            "Are you the luckiest guy to have me?",
            "Do you think we are perfect together?",
        ];

        let questionIndex = 0;

        yesBtn.addEventListener("click", () => {
            questionIndex++;
            if (questionIndex < questions.length) {
                question.innerHTML = questions[questionIndex];
                gif.src = "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif";
            } else {
                question.innerHTML = "You are the best! I love you ❤️";
                gif.src = "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif";
                audio.src = "/play_song";
                audio.play();
            }
        });

        noBtn.addEventListener("mouseover", () => {
            const randomX = Math.random() * window.innerWidth;
            const randomY = Math.random() * window.innerHeight;
            noBtn.style.left = `${randomX}px`;
            noBtn.style.top = `${randomY}px`;

            // Sprādziena efekts
            const particles = document.createElement("div");
            particles.style.position = "absolute";
            particles.style.left = `${randomX}px`;
            particles.style.top = `${randomY}px`;
            particles.style.width = "10px";
            particles.style.height = "10px";
            particles.style.background = "red";
            particles.style.borderRadius = "50%";
            document.body.appendChild(particles);

            setTimeout(() => {
                document.body.removeChild(particles);
            }, 500);
        });

        // Zvaigžņu fona efekts
        const starsContainer = document.getElementById("stars");
        for (let i = 0; i < 100; i++) {
            const star = document.createElement("div");
            star.style.left = `${Math.random() * 100}%`;
            star.style.top = `${Math.random() * 100}%`;
            star.style.animationDuration = `${Math.random() * 3 + 2}s`;
            starsContainer.appendChild(star);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/play_song', methods=['GET'])
def play_song():
    return app.send_static_file("song.mp3")

if __name__ == '__main__':
    app.run(debug=True)
