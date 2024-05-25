# backend/app/utils.py
from flask_mail import Message
from app import mail
import os

def send_reset_password_email(email, token):
    reset_password_url = f'http://localhost:3000/reset-password/change-password?token={token}'
    msg = Message('Password Reset Request', sender=os.getenv('MAIL_USERNAME'), recipients=[email])
    msg.body = (
    f"To reset your password, visit the following link:\n"
    f"{reset_password_url}\n\n"
    "This link will expire in 1 hour.\n"
    "If you did not make this request, ignore this email.\n"
    )

    try:
        mail.send(msg)
        return True
    except Exception as e:
        return False