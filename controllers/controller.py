from email.message import Message
from flask import render_template
from app import app
from models.game import *
from models.player import Player

@app.route('/home')
def index():
    return render_template('index.html', title="let's play rock paper scissors")
    
@app.route('/playgame')
def play_game():
    return render_template('play_game.html', player_1='Player 1', title='Play rock papaer scissors!')

@app.route('/<player_1_choice>')
def player2turn(player_1_choice):
    player_1 = Player("Player 1", player_1_choice)
    return render_template('player2.html', player_2="Player 2", player_1_choice=player_1_choice)


@app.route('/<player_1_choice>/<player_2_choice>')
def result(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game(player_1, player_2)
    winner = game.game_result().name
    if winner == None:
        message = "Nobody! It was a draw!"
    else:
        message = f"{winner} wins!"

    return render_template('result.html', winner=winner,
                           message=message, player_1=player_1,
                           player_2=player_2, title="and the winner is...")