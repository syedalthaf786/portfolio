from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FROM_EMAIL = "your-email@gmail.com"
PASSWORD = "your-password"

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = email
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(FROM_EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(FROM_EMAIL, email, text)
    server.quit()

    return jsonify({'message': 'Email sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
