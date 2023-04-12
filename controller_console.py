'''
controller_console.py - a Controller for TicTacToeGame, for human players using console for input.
'''
class Player:
    def __init__(self, player) -> None:
        self.player = player

    def __call__(self, game, view) -> int:
        while True:
            cell_input = view.ask_for_move(self.player)
            if cell_input == 'q':
                game.quit_game()
                break
            try:
                cell = int(cell_input)
                if cell not in game.get_valid_moves():
                    game.message('Invalid move, try again')
                    continue
                else:
                    return cell
            except ValueError:
                game.message('Invalid move, try again')
