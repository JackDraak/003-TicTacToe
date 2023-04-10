'''
console_view.py - a console View class for TicTacToeGame, for human players using a console
'''

class Viewer:
    def __init__(self, name):
        self.name = name

    def __call__(self, game):
        self.print_board(game)
        
    @staticmethod
    def print_board(game):
        print()
        for i, row in enumerate(game.board):
            formatted_row = [str((i * 3) + j + 1) if cell == ' ' else cell for j, cell in enumerate(row)]
            print(' | '.join(formatted_row))
            if i < 3 - 1:
                print('-----------------')
    
    @staticmethod
    def message(message):
        print(message)