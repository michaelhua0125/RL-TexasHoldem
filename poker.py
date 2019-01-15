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
        for _ in range(num):
            cards.append(self.deck.pop())
        return cards


class TexasHoldem(Poker):

    NUM_FLOP = 3
    NUM_TURN = 1
    NUM_RIVER = 1
    NUM_HAND = 2

    def __init__(self):
        super(TexasHoldem, self).__init__()

    def deal_hands(self):
        return self.deal(self.NUM_HAND)

    def deal_flop(self):
        self.burn_card()
        return self.deal(self.NUM_FLOP)

    def deal_turn(self):
        self.burn_card()
        return self.deal(self.NUM_TURN)

    def deal_river(self):
        self.burn_card()
        return self.deal(self.NUM_RIVER)

    def burn_card(self):
        """Put 1 card aside"""
        self.deal(1)

    def deal_public(self):
        public_cards = self.deal_flop()
        public_cards.extend(self.deal_turn())
        public_cards.extend(self.deal_river())
        return public_cards
