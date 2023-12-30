from flask import Flask, render_template, session, redirect, url_for, jsonify, request

app = Flask(__name__)
app.secret_key = 'wfshfysfgtsygt$5$%$#duhgatg&$4fayg'

def update_session():
    if 'likes' not in session:
        session['likes'] = 0


session = {
    "login": True,
    "likes": 0,
}



@app.route('/')
def indexView():
    index()
    update_session()
    return render_template('index.html', data = 0, likes=session['likes'])

@app.route('/new2')
def new1View():
    update_session()
    return render_template('index.html', data = 1)

@app.route('/new3')
def new2View():
    update_session()
    return render_template('index.html', data = 2)

@app.route('/new4')
def new3View():
    update_session()
    return render_template('index.html', data = 3)

@app.route('/new5')
def new4View():
    update_session()
    return render_template('index.html', data = 4, views_count=session['views'])

# Функції #

def index():
    session['views'] = session.get('views', 0) + 1
    views_count = session['views']
    return render_template('index.html', views_count=views_count)


@app.route('/function')
def new0FunctionView():
    update_session()
    session['likes'] += 1
    
    return redirect(url_for('indexView'))


# Очишення сесії
#@app.route('/new5/clear')
#def clear_user_session():
#    session.clear()
#    return redirect(url_for('indexView'))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8080')