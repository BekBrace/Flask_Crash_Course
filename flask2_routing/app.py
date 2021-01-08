from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, world!!!!</h1>'


@app.route('/hello')
def hello():
    return '<h1>Hello </h1>'


@app.route('/goodbye')
def goodbye():
    return '<h1>Goodbye </h1>'


if __name__ == "__main__":
    app.run(debug=True)
