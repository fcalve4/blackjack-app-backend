from app.game.player import Player
from app.game.dealer import Dealer
from app.game.deck import Deck
from app.game.deck import Card


"""
This module contains the main game logic for the Blackjack game.

Rules: S17, DAS, No Surrender, 3:2, 6D (continuous shuffle)

"""
class Game():

    def __init__(self):
        """
        Initialize the Blackjack Game instance.
        """
        self.deck = Deck() # Create a deck of cards and shuffle it
        self.deck.shuffle()

        self.player = Player("Player")
        self.dealer = Dealer()


    def deal_initial_hands(self):
        """
        Deal the initial hands to the player and dealer.
        """
        self.player.hand = [self.deck.draw_card(), self.deck.draw_card()]
        self.dealer.hand = [self.deck.draw_card(), self.deck.draw_card()]

    def check_for_naturals(self):
        """
        Check for naturals (21) in the player and dealer hands.
        """
        player_hand_value = self.get_hand_value(self.player.get_hand())
        dealer_hand_value = self.get_hand_value(self.dealer.get_hand())

        if player_hand_value == 21 and dealer_hand_value == 21:
            print("Both player and dealer have naturals!")
            return 0 # Return zero for PUSH
        if player_hand_value == 21:
            print("Player has a natural!")
            return 1 # Return one for PLAYER WIN
        if dealer_hand_value == 21:
            print("Dealer has a natural!")
            return -1 # Return negative one for DEALER WIN
        return None # Return None if no naturals


    def game_loop(self):
        """
        Main game loop to handle the flow of the poker game.
        """
        # Deal initial hands
        self.deal_initial_hands()

        # Check for naturals
        natural_result = self.check_for_naturals()
        if natural_result is not None:
            return natural_result

        # Player's turn
        player_result = self.play_player_turn()
        if player_result == 0:
            return 0
        
        # Dealer's turn
        dealer_result = self.play_dealer_turn()
        return dealer_result
        
    
