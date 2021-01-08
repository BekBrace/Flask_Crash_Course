from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    # return 'welcome %s' % name
    return f'welcome {name}'


if __name__ == '__main__':
    app.run(debug=True)


# POST
# GET
#GET /users
# HEAD
# HEAD /users
# PUT
# DELETE
