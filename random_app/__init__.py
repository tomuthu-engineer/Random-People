from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import csv
import io
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
db = SQLAlchemy(app)

# adding error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('show_user.html'), 404


# adding error handler
@app.errorhandler(500)
def something_went_wrong(e):
    return render_template('500.html'), 500