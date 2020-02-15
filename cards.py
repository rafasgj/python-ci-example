"""Implement the game 21."""

import random


class Deck:
    """Models a deck of cards."""

    def __init__(self):
        """Initialize a deck object."""
        self.cards = ['A', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'J', 'Q', 'K']

    def __iter__(self):
        """Get an iterator for the deck."""
        return self

    def __next__(self):
        """Get the next card."""
        return random.choice(self.cards)


class Dealer:  # pylint: disable=too-few-public-methods
    """Models a dealer in a 21 game."""

    def __init__(self):
        """Initialize the dealer object with an empty hand."""
        self.hand = []
        self.deck = iter(Deck())

    def new_round(self):
        """Start a new round."""

        self.hand = [next(self.deck), next(self.deck)]
