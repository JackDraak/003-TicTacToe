'''
main.py     Where all the Tic tac Toe logic functions and state are found. 
            Designed for plug-and-play Controllers (Agents) and Views, 
            so that the game can be played by humans, robots, or both for
            either fun or profit (well, maybe not profit, but it could be).
'''
from typing import List

class TicTacToeGame:    
    '''
    class TicTacToeGame - the game state, including the board, the current player, and the score matrix
    
        methods:
            __init__(self, grid_size)
            _generate_score_matrix(self, grid_size)
            get_cell_pos(self, cell_label)
            get_valid_moves(self) -> List[int]
            move(self, cell, player) -> bool
            is_winner(self, player) -> bool
            is_blocking_move(self, cell, player) -> bool
            is_draw(self) -> bool
            quit_game(self)
            __str__(self) -> str
    
    '''
    def __init__(self, grid_size):
        self.board = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.current_player = 'X' #  First player is X
        self.grid_size = grid_size
        self.score_matrix = self._generate_score_matrix(grid_size)
        
    def __str__(self):
        board_with_labels = [[str((row_idx * self.grid_size) + col_idx + 1) if cell == ' ' else cell for col_idx, cell in enumerate(row)] for row_idx, row in enumerate(self.board)]
        formatted_board = []
        for i, row in enumerate(board_with_labels):
            formatted_row = ' | '.join(row)
            if i < self.grid_size - 1:
                formatted_row += '\n' + '-' * (4 * game.grid_size - 3) 
            formatted_board.append(formatted_row)
        return "\n".join(formatted_board)
                    
    def _generate_score_matrix(self, grid_size):
        '''
        Generate a score matrix for the game board, where the score is the number of ways to win from that cell.
        '''
        assert grid_size % 2 == 1, "Grid size should be odd, comment-out this line if you feel otherwise (and good luck!)"
        matrix = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        for row in range(grid_size):
            for col in range(grid_size):
                score = 2          
                if row == col and (row == 0 or row == grid_size - 1 or row == grid_size // 2):
                    score += 1
                if row + col == grid_size - 1 and (row == 0 or row == grid_size - 1 or row == grid_size // 2):
                    score += 1
                matrix[row][col] = score
        return matrix

    def get_cell_coords_by_label(self, cell_label):
        x = (int(cell_label) - 1) // self.grid_size
        y = (int(cell_label) - 1) % self.grid_size
        return x, y
 
    def get_valid_moves(self) -> List[int]:
        moves = []
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.board[row][col] == ' ':
                    moves.append(row * self.grid_size + col + 1)
        return moves
    
    def is_blocking_move(self, cell, player):
        x, y = self.get_cell_coords_by_label(cell)
        opponent = 'X' if player == 'O' else 'O'
        if sum([1 for cell in self.board[x] if cell == opponent]) == self.grid_size - 1 and self.board[x][y] == ' ':
            return True
        if sum([1 for row in self.board if row[y] == opponent]) == self.grid_size - 1 and self.board[x][y] == ' ':
            return True
        if x == y:
            if sum([1 for i in range(self.grid_size) if self.board[i][i] == opponent]) == self.grid_size - 1 and self.board[x][y] == ' ':
                return True
        if x + y == self.grid_size - 1:
            if sum([1 for i in range(self.grid_size) if self.board[i][(self.grid_size - 1) - i] == opponent]) == self.grid_size - 1 and self.board[x][y] == ' ':
                return True
        return False
 
    def is_draw(self):
        return all([cell != ' ' for row in self.board for cell in row])
    
    def is_winner(self, player):
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(self.grid_size):
            if all([self.board[row][col] == player for row in range(self.grid_size)]):
                return True
        if all([self.board[i][i] == player for i in range(self.grid_size)]) or all([self.board[i][(self.grid_size - 1) - i] == player for i in range(self.grid_size)]):
            return True
        return False 

    def move(self, cell, player) -> bool:
        '''
        Return True if move is valid (AND claim cell, AND swap player), else False
        '''
        if cell is None:
            return False
        x, y = self.get_cell_coords_by_label(cell)
        if self.board[x][y] == ' ':
            self.board[x][y] = player
            self.current_player = 'X' if player == 'O' else 'O'
            return True
        return False
    
    def play_game(self, p1, p2, viewer):
        plays = 0
        while plays < self.grid_size ** 2:
            viewer(self)
            move = p1(self) if self.current_player == 'X' else p2(self)
            valid_move = self.move(move, self.current_player)
            if valid_move:
                plays += 1
                viewer(game)
                if self.is_winner('X'):
                    viewer.message('X wins!')
                elif self.is_winner('O'):
                    viewer.message('O wins!')
                elif self.is_draw():
                    viewer.message('Draw!')
        self.quit_game()
    
    def quit_game(self):
        print("Quitting the game...")
        raise SystemExit

                    
if __name__ == '__main__':
    #  TODO once there are more Controllers, have __main__ allow for Controller selection(s) [also applies to Viewer]
    from controller_console import Player as X
    from controller_AI_Jack import Player as O
    from view_console import Viewer as view
    GRID_SIZE = 3
    game = TicTacToeGame(GRID_SIZE)
    # play_game requires an 'X' and 'O' Controller, and a View: assigning different symbols WILL NOT WORK
    game.play_game(X('X'), O('O'), view(game))
