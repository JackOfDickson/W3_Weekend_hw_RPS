from turtle import home
from flask import render_template
from app import app
from models.player import Player

@app.route('/home')
def index():
    return render_template('index.html', title="let's play rock paper scissors")
    