class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def game_result(self):
        if player_1.choice == "rock":
            if player_2.choice == "paper":
                return False
            if player_2.choice == "scissors":
                return True
            if player_2.choice == "rock":
                return None

        if player_1.choice == "paper":
            if player_2.choice == "rock":
                return True
            if player_2.choice == "scissors":
                return False
            if player_2.choice == "paper":
                return None
        
        if player_1.choice == "scissors":
            if player_2.choice == "rock":
                return False
            if player_2.choice == "paper":
                return True
            if player_1.choice == "scissors":
                return None
