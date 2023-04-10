'''
console_controller.py - a Controller for TicTacToeGame, for human players using a console
'''

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __call__(self, game):
        while True:
            try:
                x, y = map(int, input('Enter coordinates x, y for your next move (1-3): ').split())
                if game.move(x - 1, y - 1, self.symbol):
                    break
                else:
                    print('Invalid move, try again')
            except ValueError:
                print('Invalid move, try again')
        