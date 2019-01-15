from texas_holdem import *
from score import *
from player import *

class Game:


    NUM_FLOP = 3
    NUM_TURN = 1
    NUM_RIVER = 1
    NUM_HAND = 2

    def __init__(self, players, sb_bet=10):
        self.deck = TexasHoldem()
        self.sb_bet = sb_bet
        self.bb_bet = 2 * self.sb_bet
        self.min_bet = self.bb_bet
        self.players = players
        self.active_players = self.get_active_players()
        self.dealer = 0 #the first player should be dealer
        self.public = []
        self.start()

    def __str__(self):
        # should show the game states
        # i.e. Small Blind, Big Blind, Dealer;
        # public cards, current players, etc.
        pass

    def get_active_players(self):
        return [player for player in self.players if player.in_game]

    def start(self):
        # deal hand
        hands = self.deck.deal_hands(len(self.players))
        for player in self.players:
            hand = [hands.pop() for i in range(self.deck.hand_num)]
            player.get_hand(hand)
        # wait for players' actions (call or fold or raise)
        self.deal_flop()
        # wait for players' actions (call or fold or raise)
        self.deal_turn()
        # wait for players' actions (call or fold or raise)
        self.deal_river()
        # wait for players' actions (call or fold or raise)



    def deal_flop(self):
        self.public.append(self.deck.deal_flop())

    def deal_turn(self):
        self.public.append(self.deck.deal_turn())

    def deal_river(self):
        self.public.append(self.deck.deal_river())

    def show_public(self):
        print('Current public cards:\n')
        print(' '.join(self.public))

    def get_players_action(self):
        for player in self.active_players:
            player.get_action()
        pass
