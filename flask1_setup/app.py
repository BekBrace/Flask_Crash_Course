from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, world!!!!</h1>'


# 1st way to run your file by set FLASK_APP=app.py / flask run
# 1st way to debug is to set FLASK_APP=development
# export --> for MAc/Linux users

# 2d way to run your file and debugging is by typing the following:
# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
