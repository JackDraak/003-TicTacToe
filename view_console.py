'''
view_console.py - a console View class for TicTacToeGame, for human players using a console
'''
class Viewer:
    def __init__(self, game) -> None:
        self.game = game
    
    def __call__(self) -> None:
        print()
        print(self.game) 
        
    def ask_to_continue(self) -> bool:
        while True:
            continue_playing = input('Continue playing? (Y/n): ')
            if continue_playing == 'y' or continue_playing == '':
                return True
            elif continue_playing == 'n':
                return False
            else:
                self.message('Invalid input, try again')
                continue
    
    def ask_for_move(self, player) -> int:
        while True:
            cell_input = input(f'{player} - Enter the cell number for your next move {self.game.get_valid_moves()} or "q" to quit: ')
            if cell_input == 'q':
                self.game.quit_game()
                break
            try:
                cell = int(cell_input)
                if cell not in self.game.get_valid_moves():
                    self.message('Invalid move, try again')
                    continue
                else:
                    return cell
            except ValueError:
                self.message('Invalid move, try again')

    @staticmethod
    def message(message) -> None:
        print(message)
