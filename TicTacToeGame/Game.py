'''
Game.py - where all the logic should go, including the game loop, and the game state.
Designed for plug-and-play Controllers and Views, so that the game can be played by humans, robots, or both
'''
#  TODO once there are more Controllers, have __main__ allow for Controller selection(s) [also applies to Viewers]
from console_controller import Player as p1
from AI_Jack_controller import Player as p2
from console_view import Viewer as view

GRID_SIZE = 3 #  Needs to be an odd number (=>3) for Jack algorithm to work
SCORE_MATRIX = [[GRID_SIZE - abs(i - j) for j in range(GRID_SIZE)] for i in range(GRID_SIZE)] 

class TicTacToeGame:    
    def __init__(self):
        self.board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.current_player = 'X' #  First player is X

    def play_game(self, player1, player2):
        while True:
            view.print_board(self)
            if self.current_player == 'X':
                player1(self)
            else:
                player2(self)
            if self.is_winner('X'):
                view.message('X wins!')
                break
            elif self.is_winner('O'):
                view.message('O wins!')
                break
            elif self.is_draw():
                view.message('Draw!')
                break

    #  Convert x, y coordinates to cell number, 1-9
    def get_cell_number(self, x, y):
        return x * 3 + y + 1

    #  return True if move is valid (and claim cell, and swap player), else False
    def move(self, x, y, player):
        if self.board[x][y] == ' ':
            self.board[x][y] = player
            self.current_player = 'X' if player == 'O' else 'O'
            return True
        return False
    
    #  return list of valid_moves (cells) on self.board       
    def valid_moves(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    actions.append(i * 3 + j)
        return actions

    #  Typical Tic-Tac-Toe blocking move of opposing player having 2 in a row, column, or diagonal
    def is_blocking_move(self, x, y, player):
        pass

    #  Typical Tic-Tac-Toe win condition of one player having 3 in a row, column, or diagonal
    def is_winning_move(self, x, y, player):
        if all([self.board[x][i] == player for i in range(3)]):
            return True
        elif all([self.board[i][y] == player for i in range(3)]):
            return True
        elif all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        else:
            return False
    
    #  Typical Tic-Tac-Toe draw conditions of self.board full   
    def is_draw(self):
        return all([cell != ' ' for row in self.board for cell in row])
    
    #  Typical Tic-Tac-Toe win condition of one player having 3 in a row, column, or diagonal
    def is_winner(self, player):
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        return False
    
    #  If there is a winning move, return it, 
    #  else if there is a blocking move, return the highest priority blocking move, 
    #  else return (one of) the highest priority move
    def best_moves(self):
        pass
    
    #  string representation of self.board for humans (or robots) to read, format nicely, with numbered cells, 1-9
    def __str__(self):
        return "\n".join([' | '.join(row) for row in self.board])
             
             
game = TicTacToeGame()
                
#  TODO once there are more Controllers, have __main__ allow for Controller selection(s) [also applies to Views]            
if __name__ == '__main__':
    game = TicTacToeGame()
    game.play_game(p1, p2)
