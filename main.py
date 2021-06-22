from flask import Flask
app = Flask(__name__)


@app.route("/")
def greet():
    return "Good Morning"


if __name__ == "__main__":
    app.run(debug=True, port=7000)
