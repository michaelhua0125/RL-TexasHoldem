from texas_holdem import *
from score import *
from player import *
from game import *

if __name__ == "__main __":
    num_players = 2
    players = []
    for i in range(num_players):
        player = Player()
        players.append(player)
    
    for player in players:
        player.play_game()
    
    game = Game(players)