class Player:
    """ Class for defining player behavior

        Player should respond to the following behavior:
        1) raise: 
            bet some amount of chips, which should be greater than
            minium bet but no greater than player's current chips
        2) fold:
            player quit the current game and lose all his/her bet
        3) call:
            call(bet) the largest bet of current round
    """

    def __init__(self, name, chips=500):
        self.name = name
        self.chips = 500
        self.in_game = False
        self.hand = None

    def __str__(self):
        line = f'Chips: {self.chips}, In Game: {self.in_game} Current Hand: {self.hand}'
        return line

    def play_game(self):
        self.in_game = True

    def bet(self, chips):
        if chips > self.chips:
            print('You don\'t have enough chips. Will bet All-in')
            chips = self.chips
        self.chips -= chips
        print(f'{self.name} has bet {chips}')
        return chips

    def fold(self):
        self.in_game = False
        print(f'Player {self.name} has fold')

    def get_hand(self, cards):
        self.hand = cards

    def current_hand(self):
        return self.hand

    def get_action(self, current_bet):
        valid_actions = ['a', 'c', 'f', 'r']
        instruction = 'r for raise; f for fold; c for call; a for all-in.\nEnter your action: '
        action = input(instruction).lower()
        while action not in valid_actions:
            print('Invalid action, retry.')
            action = input(instruction).lower()
        if action == 'r':
            chips = int(eval(input('Enter your bet amount: ')))
            self.bet(chips)
            return self.bet(chips)
        elif action == 'a':
            return self.bet(self.chips)
        elif action == 'f':
            self.fold()
        else:
            self.bet(current_bet)

