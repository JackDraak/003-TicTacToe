## Tic Tac Toe (python)

 - main.py - This file contains the TicTacToeGame class that implements the logic for the Tic Tac Toe game, such as the game board, state, and the score matrix. It also includes methods to handle moves, check for a winner or draw, and play the game with different controllers and views.

 - controller_console.py - This file contains a Player class that acts as a controller for human players using a console. It takes input from the user to make a move.

 - controller_AI_Jack.py - This file contains a Player class that acts as a controller for an AI player using the AI_Jack algorithm. The AI_Jack algorithm works as follows:

>
> If there's a winning move, play it.
>
> If there are blocking moves, play one from the set with the highest score matrix.
>
> If there are no blocking moves, play a random move from the set with the highest score matrix.
>

 - view_console.py - This file contains a Viewer class that provides a console view for the Tic Tac Toe game. It prints the current game board and messages on the console.

In the current implementation, the game is set up with a human player using the console controller for 'X', an AI player using the AI_Jack controller for 'O', and a console view to display the game board and messages. The game is played on a *3x3 grid. *(attempting to keep it playable at other grid sizes, as well...)