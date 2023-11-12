from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/imt')
def about():
    return render_template("IMT.html")

@app.route('/cnt_calorie1')
def cnt1():
    return render_template("cnt1.html")

@app.route('/cnt_calorie2')
def cnt2():
    return render_template("cnt2.html")





if __name__ == '__main__':
    app.run(debug=True)