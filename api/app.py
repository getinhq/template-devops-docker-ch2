from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    # TODO: optionally read/write SQLite under /data
    return {"status": "ok", "message": "Implement API per README"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
