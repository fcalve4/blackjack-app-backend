class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def is_bust(self):
        """
        Check if the player's hand is bust (over 21).
        :return: True if the hand is bust, False otherwise.
        """
        return self.get_hand_value() > 21


    def do_action(self, action):
        """
        Perform an action.
        :param action: The action to be performed.
        :return: None
        """
        print(f"{self.name} performs action: {action}")

    def get_hand(self):
        """
        Get the player's hand.
        :return: The player's hand (list of card objects).
        """
        return self.hand
    
    def get_hand_value(self):
        total = 0
        aces = 0

        for card in self.hand:
            if card == 'A':
                aces += 1
                total += 11
            else:
                total += card

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total, 'soft' if aces else 'hard'

    def __repr__(self):
        return f"{self.name}: {self.hand}"
