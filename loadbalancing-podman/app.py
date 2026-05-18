from flask import Flask
import os
import socket

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "UNKNOWN")

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"Hello dari {APP_NAME} | Host: {hostname}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
