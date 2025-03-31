class Dealer:
    def __init__(self):
        self.hand = []


    def do_action(self, action):
        """
        Perform an action.
        :param action: The action to be performed.
        :return: None
        """
        print(f"{self.name} performs action: {action}")

    def get_hand(self):
        """
        Get the dealer's hand.
        :return: The dealer's hand (list of card objects).
        """
        return self.hand

    def __repr__(self):
        return f"{self.name}: {self.hand}"
