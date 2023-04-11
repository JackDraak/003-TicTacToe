'''
controller_console.py - a Controller for TicTacToeGame, for human players using a console
'''
class Player:
    def __init__(self, player) -> None:
        self.player = player

    def __call__(self, game) -> int:
        while True:
            cell_input = input('Enter the cell number for your next move (1-9) or "q" to quit: ')
            if cell_input == 'q':
                game.quit_game()
                break
            try:
                cell = int(cell_input)
                if cell not in game.get_valid_moves():
                    print('Invalid move, try again')
                    continue
                else:
                    return cell
            except ValueError:
                print('Invalid move, try again')
