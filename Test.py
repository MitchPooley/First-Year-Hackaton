from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def flask_hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run(port=8000, debug=True)