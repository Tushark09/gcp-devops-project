from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer']
    if answer == 'YES':
        return "I love you so much"
    elif answer == 'NO':
        return "Sorry to say that, You missed an opportunity !!"
    else:
        return "Invalid answer"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
