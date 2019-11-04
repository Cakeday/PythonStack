import random, math
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'security is cool'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try Again"

@app.route('/')
def visit():
    session['answer']=random.randint(1,100)
    session['counter']=1
    return render_template('index.html')

# @app.route('/count')
# def count_init():
#     session['counter']+=1
#     session['actual_page_visits']+=1
#     return render_template('index.html')

@app.route('/guess', methods=['POST'])
def choose():
    answer_key='None'
    # int(request.form['howmuch'])
    math.floor(float(request.form['howmuch']))

    session['counter']+=1
    counter=session['counter']

    if int(counter) == 5:
        answer_key='<h3 class="text-light bg-danger py-5 col-2 offset-5"> are you frikn srs </h3>'
        return render_template('index.html', answer_key=answer_key)
        # i could totally add another html page that forces them to try again but ehh

    if float(request.form['howmuch']) < session['answer']:
        answer_key='<h3 class="text-light bg-danger py-5 col-2 offset-5"> Too Low </h3>'
        print(answer_key)
        return render_template('index.html', answer_key=answer_key, counter=counter)
    if float(request.form['howmuch']) > session['answer']:
        answer_key='<h3 class="text-light bg-danger py-5 col-2 offset-5"> Too High </h3>'
        return render_template('index.html', answer_key=answer_key, counter=counter)
    if float(request.form['howmuch']) == session['answer']:
        x=session['answer']
        answer_key=f'<div class="bg-success py-5 col-2 offset-5"><h3 class="text-light"> about frikn time. the number was {x}!</h3></div>'
        return render_template('index.html', answer_key=answer_key, counter=counter)
        # i could also add a button with a form that resets the game but also ehh

# @app.route('/count2', methods=['POST'])
# def count_two():
#     session['counter']+=1
#     return redirect('/count')

# @app.route('/destroy_session', methods=['POST'])
# def destroy():
#     session.clear()
#     return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)