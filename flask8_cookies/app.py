from flask import Flask, request, make_response, render_template
app = Flask(__name__)


@ app.route('/')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        res = make_response(render_template('readcookie.html'))
        res.set_cookie('userID', user)
        return res


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome '+name+' | This is your cookie!!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
