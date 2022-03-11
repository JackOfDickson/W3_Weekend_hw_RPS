from flask import render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/home')
def index():
    return render_template('index.html', title="let's play rock paper scissors")
    
@app.route('/playgame')
def play_game():
    return render_template('play_game.html')


@app.route('/<player_1_choice>/<player_2_choice>')
def result():
    player_1 = Player("player_1", player_1_choice)
    player_2 = Player("player_2", player_2_choice)
    game = Game(player_1, player_2)
    winner = game
    return render_template('result.html', winner=winner)