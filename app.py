from flask import Flask, render_template, request
import db

app = Flask(__name__)

def stringToFloat(value):
    v = float(value)
    return v

#home route: Displays the index form for input
@app.route('/')
def index():
    return render_template('index.html')

#success route displays the results store in the db
@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["user_email"]
        height = stringToFloat(request.form["user_height"])
        weight = stringToFloat(request.form["user_weight"])
        if (height != 0) and (weight > 0):#if entered height is 0 and weight is greater than 0
            bmi = weight/(height*height)
            bmi = ("%.2f" % bmi)
            db.insert(email, height, weight, bmi)
            print(db.search(email))
            return render_template('success.html', email=db.search(email)[-1][1], height=db.search(email)[-1][2], weight=db.search(email)[-1][3]
                                   , bmi=db.search(email)[-1][4])
        else:
            return '<h1>Height or Weight can not be zero</h1>'


if __name__ == '__main__':
    app.debug = True
    app.run()
