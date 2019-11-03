from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'security is cool'

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')[]
# def catch_all(path):
#     return "Sorry! No response. Try Again"

@app.route('/')
def visit():
    session['counter']=0
    session['actual_page_visits']=0
    return redirect('/count')

# @app.route('/')
# def visit():
#     return render_template('index.html')

@app.route('/count')
def count_init():
    session['counter']+=1
    session['actual_page_visits']+=1
    return render_template('index.html')

@app.route('/count2', methods=['POST'])
def count_two():
    session['counter']+=1
    return redirect('/count')

@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

@app.route('/choose', methods=['POST'])
def choose():
    session['counter']-=1
    session['counter']+=int(request.form['howmuch'])
    return redirect('/count')


if __name__ == "__main__":
    app.run(debug=True)