import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SECRET_KEY = '2968feeae67a361389810fb05173bc8d'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')