from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["user_email"]
        height = request.form["user_height"]
        weight = request.form["user_weight"]
        bmi = float(weight)/(float(height)*float(height))
        return render_template('success.html', email=email, height=height, weight=weight, bmi=bmi)


if __name__ == '__main__':
    app.debug = True
    app.run()
