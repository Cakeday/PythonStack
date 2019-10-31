from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try Again"


@app.route('/')
def display_init():
    return render_template('index.html')









if __name__ == "__main__":
    app.run(debug=True)