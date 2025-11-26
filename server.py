from flask import Flask
import os

app = Flask(__name__)

@app.route("/deploy", methods=["POST"])
def deploy():
    print("🚀 Received deploy trigger. Pulling latest code...")
    os.system("git pull")
    os.system("python3 app.py")
    return "Deployed", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
