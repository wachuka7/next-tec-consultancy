from os import environ
from flask import Flask

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'sqlite:///consultancy.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get('SECRET_KEY') or 'your_secret_key'  # Replace with a strong secret key


