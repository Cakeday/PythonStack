from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try Again"


@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>')
def hello(name):
    print(name)
    print(id)
    return 'Hi ' + name

@app.route('/repeat/<int:num>/<word>')
def so_many_words(num, word):
    repeat = ''
    for val in range(int(num)):
        repeat += f'<h3>{word}</h3>'
    return repeat



if __name__=="__main__": 
    app.run(debug=True)  