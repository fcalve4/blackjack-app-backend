from app.game.player import Player

class Dealer(Player):
    def __init__(self):
        self.hand = []


    def get_dealer_upcard(self):
        return self.hand[0]