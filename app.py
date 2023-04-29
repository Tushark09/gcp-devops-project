# app.py
from flask import Flask, render_template, request
import smtplib

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer']
    if answer == 'yes':
        response = "I love you so much!"
    elif answer == 'no':
        response = "Sorry to say that, You missed an opportunity !!"
    elif answer == 'maybe':
        response = "Let's see how things go!"
    elif answer == 'not sure':
        response = "Take your time and think it over!"
    else:
        response = "I didn't understand your answer."
        
    # Send email with the response
    try:
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "tusharkuchekar2014@gmail.com"
        receiver_email = "tusharkuchekar2014@gmail.com"
        password = "Tushu@0805"
        message = f"Subject: Response\n\n{response}"
        
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(f"Error while sending email: {e}")
    finally:
        server.quit()

    return "Thanks for your response! You'll receive the answer in your email shortly."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')