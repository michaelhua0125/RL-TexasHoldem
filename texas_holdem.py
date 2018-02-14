import poker

class TexasHoldem(poker.Poker):
    def __init__(self):
        super(TexasHoldem, self).__init__()
        self.hand_num = 2
        self.flop_num = 3
        self.turn_num = 1
        self.river_num = 1
        self.burn_num = 1

    def deal_hands(self, players):
        return self.deal(self.hand_num * players)

    def deal_flop(self):
        self.burn_card()
        return self.deal(self.flop_num)

    def deal_turn(self):
        self.burn_card()
        return self.deal(self.turn_num)

    def deal_river(self):
        self.burn_card()
        return self.deal(self.river_num)

    def burn_card(self):
        return self.deal(self.burn_num)

    def deal_public(self):
        public_cards = self.deal_flop()
        public_cards.extend(self.deal_turn())
        public_cards.extend(self.deal_river())
        return public_cards



if __name__ == '__main__':
    deck = TexasHoldem()
    print(deck)
    print(deck.deal_public())
