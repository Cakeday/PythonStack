from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try Again"




@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:num>')
def multipleboxes(num):
    if num > 3:
        num -= 3
        repeat=''
        for val in range (int(num)):
            repeat += '<div class="blue">Placeholder Text</div>'
        return render_template('index.html',repeat=repeat)

@app.route('/play/<int:num>/<color>')
def multiple_colored_boxes(num,color):
    if num > 3:
        num -= 3
        color_repeat=''
        for val in range (int(num)):
            color_repeat += f'<div class="blue" style="background-color: {color};">Placeholder Text</div>'
        return render_template('index.html',color_repeat=color_repeat)






if __name__ == "__main__":
    app.run(debug=True)