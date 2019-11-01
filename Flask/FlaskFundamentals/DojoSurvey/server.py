from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try Again"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    gender_from_form = request.form['gender']
    return render_template("result.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, comment_on_template=comment_from_form, gender_on_template=gender_from_form)





if __name__ == "__main__":
    app.run(debug=True)