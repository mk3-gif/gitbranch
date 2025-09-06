import os
import random
import socket
from flask import Flask, render_template

app = Flask(__name__)

# Predefined color codes
COLOR_CODES = {
    "blue": "#2980b9",
}

# Select color: from env var or random choice
color = os.getenv("APP_COLOR", random.choice(list(COLOR_CODES.keys())))

@app.route("/")
def home():
    """Default route showing hostname and color."""
    return render_template(
        "hello.html",
        name=socket.gethostname(),
        color=COLOR_CODES[color]
    )

@app.route("/color/<new_color>")
def change_color(new_color):
    """Change color dynamically by visiting /color/<new_color>."""
    if new_color not in COLOR_CODES:
        return f"Color '{new_color}' not supported!", 400
    return render_template(
        "hello.html",
        name=socket.gethostname(),
        color=COLOR_CODES[new_color]
    )

@app.route("/read_file")
def read_file():
    """Reads and displays contents of /data/testfile.txt."""
    file_path = "/data/testfile.txt"
    try:
        with open(file_path, "r") as f:
            contents = f.read()
    except FileNotFoundError:
        contents = f"File {file_path} not found!"
    return render_template(
        "hello.html",
        name=socket.gethostname(),
        contents=contents,
        color=COLOR_CODES[color]
    )

if __name__ == "__main__":
    # Run the app on port 8080, accessible from outside the container
    app.run(host="0.0.0.0", port=8080, debug=True)

