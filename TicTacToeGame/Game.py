'''
Game.py - where all the logic should go, including the game loop, and the game state.
Designed for plug-and-play Controllers and Views, so that the game can be played by humans, robots, or both
'''
#  TODO once there are more Controllers, have __main__ allow for Controller selection(s) [also applies to Viewers]
from typing import List
from console_controller import Player as p1 # X
from AI_Jack_controller import Player as p2 # O
from console_view import Viewer as view

GRID_SIZE = 3 #  Needs to be an odd number (=>3) for Jack algorithm to work
SCORE_MATRIX = [[GRID_SIZE - abs(i - j) for j in range(GRID_SIZE)] for i in range(GRID_SIZE)] 

class TicTacToeGame:    
    def __init__(self):
        self.board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.current_player = 'X' #  First player is X

    def play_game(self, p1, p2, viewer):
        while True:
            # print game board here:
            viewer.print_board(self)
            # toggle between p1 and p2 controllers each loop
            move = p1(self) if self.current_player == 'X' else p2(self)
            
            if self.move(*move, self.current_player):
                if self.is_winner('X'):
                    viewer.message('X wins!')
                    break
                elif self.is_winner('O'):
                    viewer.message('O wins!')
                    break   
                elif self.is_draw():
                    viewer.message('Draw!')
                    break
            else:
                viewer.message('Invalid move, try again')

    def get_cell_coordinates(self, cell_label):
        x = (int(cell_label) - 1) // 3
        y = (int(cell_label) - 1) % 3
        return x, y

    #  return True if move is valid (and claim cell, and swap player), else False
    def move(self, cell, player):
        if cell is None:
            return False
        x, y = self.get_cell_coordinates(cell)
        if self.board[x][y] == ' ':
            self.board[x][y] = player
            self.current_player = 'X' if player == 'O' else 'O'
            return True
        return False
    
    #  return list of valid_moves (cells) on self.board       
    def valid_moves(self) -> List[int]:
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
    game.play_game(p1('Human', 'X'), p2('AI_Jack', 'O'), view(game))
