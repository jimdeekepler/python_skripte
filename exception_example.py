

class Game(object):
    def __init__(self):
        self.players = []

    def init_players(self, num_players=5):
        print('Number of players:', num_players, range(num_players))
        for f in range(num_players):
            self.players.append(Player())


class Player(object):
    def __init__(self, name='John Doe', points=0):
        self.name = name
        self.points = points

        1 / 0  # raise ArithmeticError

g = Game()
g.init_players()
