'''
main.py     Where all the Tic tac Toe logic functions and state are found. 
            Designed for plug-and-play Controllers (Agents) and Views, 
            so that the game can be played by humans, robots, or both for
            either fun or profit (well, maybe not profit, but it could be).
'''
from typing import List
from view_console import Viewer

class TicTacToeGame:    
    '''
    class TicTacToeGame - the game board and state, including the current player, 
    and the score matrix which evaluates each cell based on its strategic value.
    '''
    def __init__(self, grid_size) -> None:
        self.grid_size = grid_size
        self.board = self._generate_board()
        self.current_player = 'X' #  First player is X
        self.score_matrix = self._generate_score_matrix(grid_size)
        
    def __str__(self) -> str:
        board_with_labels = [[f'{(row_idx * self.grid_size) + col_idx + 1:2d}' if cell == ' ' else f'{cell:^2s}' for col_idx, cell in enumerate(row)] for row_idx, row in enumerate(self.board)]
        formatted_board = []
        for i, row in enumerate(board_with_labels):
            formatted_row = ' | '.join(row)
            if i < self.grid_size - 1:
                formatted_row += '\n' + '-' * (5 * game.grid_size - 3) 
            formatted_board.append(formatted_row)
        return "\n".join(formatted_board)
    
    def _count_symbols_in_line(self, player, coords):
        count = 0
        for x, y in coords:
            if self.board[x][y] == player:
                count += 1
        return count
    
    def _generate_board(self):
        return [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]              
        
    def _generate_score_matrix(self, grid_size) -> List[List[int]]:
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
    
    def is_blocking_move(self, cell, player) -> bool:
        x, y = self.get_cell_coords_by_label(cell)
        opponent = 'X' if player == 'O' else 'O'
        lines = [
            [(x, col) for col in range(self.grid_size)],
            [(row, y) for row in range(self.grid_size)],
        ]
        if x == y:
            lines.append([(i, i) for i in range(self.grid_size)])
        if x + y == self.grid_size - 1:
            lines.append([(i, self.grid_size - 1 - i) for i in range(self.grid_size)])
        for line in lines:
            if self._count_symbols_in_line(opponent, line) == self.grid_size - 1 and self.board[x][y] == ' ':
                return True
        return False
 
    def is_draw(self) -> bool:
        return not (self.is_winner('X') or self.is_winner('O')) and all([cell != ' ' for row in self.board for cell in row])

    def is_winner(self, player) -> bool:
        lines = [[(row, col) for col in range(self.grid_size)] for row in range(self.grid_size)] + [[(row, col) for row in range(self.grid_size)] for col in range(self.grid_size)] + [[(i, i) for i in range(self.grid_size)], [(i, self.grid_size - 1 - i) for i in range(self.grid_size)],]
        for line in lines:
            if self._count_symbols_in_line(player, line) == self.grid_size:
                return True
        return False
    
    def is_winning_move(self, cell, player) -> bool:
        x, y = self.get_cell_coords_by_label(cell)
        lines = [[(x, col) for col in range(self.grid_size)],[(row, y) for row in range(self.grid_size)],]
        if x == y:
            lines.append([(i, i) for i in range(self.grid_size)])
        if x + y == self.grid_size - 1:
            lines.append([(i, self.grid_size - 1 - i) for i in range(self.grid_size)])
        for line in lines:
            if self._count_symbols_in_line(player, line) == self.grid_size - 1 and self.board[x][y] == ' ':
                return True
        return False
    
    def message(self, msg) -> None:
        Viewer.message(msg)

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
    
    def play_game(self, p1, p2, viewer) -> None:
        view = viewer(self)
        view()
        turn = 0
        while turn < self.grid_size ** 2:
            if self.current_player == 'X': 
                move = p1(self, view)
            else:
                move = p2(self, view) 
            print(f"turn {turn + 1}: Player {self.current_player} played {move}")
            valid_move = self.move(move, self.current_player)
            if valid_move:
                turn += 1
                view()
                if self.is_winner('X'):
                    view.message('X wins!')
                elif self.is_winner('O'):
                    view.message('O wins!')
                elif self.is_draw():
                    view.message('Draw!')
            if self.is_winner('X') or self.is_winner('O') or self.is_draw():
                break   
        continue_playing = view.ask_to_continue()
        if not continue_playing:
            self.quit_game()
        else:
            self.board = self._generate_board()
            self.current_player = 'X'

    def quit_game(self) -> None:
        print("Quitting the game...")
        exit()

                    
#  TODO once there are more Controllers, have __main__ allow for Controller selection(s) [also applies to Viewer]
if __name__ == '__main__':
    from controller_console import Player as X
    from controller_AI_Jack import Player as O
    GRID_SIZE = 3   
    game = TicTacToeGame(GRID_SIZE)
    while True:
        # play_game requires an 'X' and 'O' Controller, and a View: assigning different symbols WILL NOT WORK
        game.play_game(X('X'), O('O'), Viewer)
    