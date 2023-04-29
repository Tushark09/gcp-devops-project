from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer']
    if answer == 'yes':
        return "I love you so much!"
    elif answer == 'no':
        return "Sorry to say that, You missed an opportunity !!"
    elif answer == 'maybe':
        return "Let's see how things go!"
    elif answer == 'not sure':
        return "Take your time and think it over!"
    else:
        return "I didn't understand your answer."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
