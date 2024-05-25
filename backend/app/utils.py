# backend/app/utils.py
from flask_mail import Mail, Message
from app import mail
import os

def send_reset_password_email(email, token):
    msg = Message('Password Reset Request', sender=os.getenv('MAIL_USERNAME'), recipients=[email])
    msg.body = f'Click the following link to reset your password: http://localhost:3000/reset-password/{token}'
    try:
        mail.send(msg)
        return True
    except Exception as e:
        return False