
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def employee():
    return render_template('employee.html')


@app.route('/report', methods=['POST', 'GET'])
def report():
    if request.method == 'POST':
        report = request.form
        return render_template("report.html", report=report)


if __name__ == '__main__':
    app.run(debug=True)
