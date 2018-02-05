from flask import Flask, render_template, request
import db

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
        db.insert(email, height, weight, bmi)
        print(db.search(email))
        return render_template('success.html', email=db.search(email)[-1][1], height=db.search(email)[-1][2], weight=db.search(email)[-1][3]
                               , bmi=db.search(email)[-1][4])


if __name__ == '__main__':
    app.debug = True
    app.run()
