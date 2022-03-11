from turtle import home
from flask import render_template
from app import app
from models.player import Player

@app.route('/home')
def index():
    return render_template('index.html', title="let's play rock paper scissors")
    
@app.route('/player1')
def player_1_turn():
    return render_template('player_1_turn.html')

@app.route('/{player_1_choice}/player2')
def player_2_turn():
    return render_template('player_2_turn.html')

@app.route('/{player_1_choice}/{player_2_choice}')
def result():
    return render_template('result.html')