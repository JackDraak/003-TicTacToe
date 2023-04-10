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
                cell = int(input('Enter the cell number for your next move (1-9): '))
                if game.move(cell, self.symbol):
                    break
                else:
                    print('Invalid move, try again')
            except ValueError:
                print('Invalid move, try again')