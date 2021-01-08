from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return render_template('index.html', name=name)


@app.route('/2021')
def new_year():
    return '<h1>Happy New Year 2021!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
