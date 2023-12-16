from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def indexView():
    return render_template('index.html', data = 0)

@app.route('/new2')
def new1View():
    return render_template('index.html', data = 1)

@app.route('/new3')
def new2View():
    return render_template('index.html', data = 2)

@app.route('/new4')
def new3View():
    return render_template('index.html', data = 3)

@app.route('/new5')
def new4View():
    return render_template('index.html', data = 4)






if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8080')