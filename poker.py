import random

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'S', 'C']

class Poker:
    def __init__(self):
        self.deck = self.reset()
        self.shuffle_deck()

    def __str__(self):
        num = len(self.deck)
        if num == 1:
            base = ' card left: \n'
        else:
            base = ' cards left: \n'
        return str(num) + base + ' '.join(self.deck)

    def reset(self):
        return [''.join([r, s]) for r in RANKS for s in SUITS]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal(self, num):
        cards = []
        for i in range(num):
            cards.append(self.deck.pop())
        return cards
