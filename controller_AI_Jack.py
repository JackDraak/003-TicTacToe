'''
controller_AI_Jack.py - a Controller for TicTacToeGame, using the AI_Jack algorithm

    Player(game)
        It returns a valid move for the current player, or None if there are no valid moves. It interrogates 
        the game object for valid moves, and then applies the AI_Jack algorithm with other game methods to 
        determine the best move, using a score matrix to fine-tune the algorithm.
'''
import random

class Player:
    '''
    Player class for TicTacToeGame  -  uses the AI_Jack algorithm:
    
        1. if there is a winning move, play it, otherwise...
        2. if there are blocking moves, play one from the set with the highest score matrix, otherwise...
        3. play a move from the set with the highest score matrix
    
    score matrix is a 2D array of relative values for each move, based on the number of possible winning lines
    '''
    def __init__(self, player):
        self.player = player

    def __call__(self, game):   
        moves = game.get_valid_moves()
        if len(moves) == 0:
            print('AI_Jack: No valid moves!')
            return None
        if len(moves) == 1:
            print('AI_Jack: Last valid move!')
            return moves[0]
        # 1. if there is a winning move, play it
        for move in moves:
            if game.is_winning_move(move, self.player):
                print('AI_Jack: Winning move!')
                return move
        # 2. if there are blocking moves, play one from the set with the highest score_matrix
        blocking_moves = []
        for move in moves:
            if game.is_blocking_move(move, self.player):
                blocking_moves.append(move)
        if len(blocking_moves) > 0:
            max_score = 0
            best_moves = []
            for move in blocking_moves:
                x, y = game.get_cell_coords_by_label(move)
                score = game.score_matrix[x][y]
                if score > max_score:
                    max_score = score
                    best_moves = [move]
                elif score == max_score:
                    best_moves.append(move)
            print('AI_Jack: Blocking move!')
            return random.choice(best_moves)    
        # 3. if there are no blocking moves, play a random move from the set with the highest score_matrix
        max_score = 0
        best_moves = []
        for move in moves:
            x, y = game.get_cell_coords_by_label(move)
            score = game.score_matrix[x][y]
            if score > max_score:
                max_score = score
                best_moves = [move]
            elif score == max_score:
                best_moves.append(move)
        print("AI_Jack: I'll try this!")
        return random.choice(best_moves)
