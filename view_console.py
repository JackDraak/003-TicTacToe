'''
view_console.py - a console View class for TicTacToeGame, for human players using a console
'''
class Viewer:
    def __init__(self, game):
        self.game = game
    
    def __call__(self, game):
        print()
        print(game) 

    @staticmethod
    def message(message):
        print(message)
