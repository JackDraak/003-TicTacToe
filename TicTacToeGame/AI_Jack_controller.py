'''
AI_Jack_controller.py - a Controller for TicTacToeGame, using the Jack algorithm
'''

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score_matrix = [[3 - abs(i - j) for j in range(3)] for i in range(3)]

    def __call__(self, game):
        #  TODO implement Jack algorithm using Game class methods as follows (1, 2, 3):
        
        #  1. Win if possible, else
        valid_moves = game.get_actions() #  returns current list of available actions (cells) on self.board
        for move in valid_moves:
            x = move // 3
            y = move % 3
            if game.is_winning_move(x, y, self.symbol):
                game.move(x, y, self.symbol)
                break
            
        #  2. TODO Block if possible: take one move from highest-score valid_moves blocking moves using game.SCORE_MATRIX, else
        for move in valid_moves:
            x = move // 3
            y = move % 3
            if game.is_blocking_move(x, y):
                # TODO comlete this
                pass

        #  3. TODO Take one move from highest-score valid_moves using game.SCORE_MATRIX:
        for move in valid_moves:
            x = move // 3
            y = move % 3
            if game.move(x, y, self.symbol):
                # TODO comlete this
                break
            
            
