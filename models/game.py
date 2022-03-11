class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def game_result(self):
        if self.player_1.choice == "rock":
            if self.player_2.choice == "paper":
                return self.player_2
            if self.player_2.choice == "scissors":
                return self.player_1
            if self.player_2.choice == "rock":
                return None

        if self.player_1.choice == "paper":
            if self.player_2.choice == "rock":
                return self.player_1
            if self.player_2.choice == "scissors":
                return self.player_2
            if self.player_2.choice == "paper":
                return None
        
        if self.player_1.choice == "scissors":
            if self.player_2.choice == "rock":
                return self.player_2
            if self.player_2.choice == "paper":
                return self.player_1
            if self.player_1.choice == "scissors":
                return None
