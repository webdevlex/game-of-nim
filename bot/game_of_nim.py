from bot.games import *


class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3, 1]):
        moves = self.generate_all_moves(board)
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=moves)

    def generate_all_moves(self, board):
        """Generate all possible moves from the current board."""
        moves = []
        for i, n in enumerate(board):
            if n > 0:
                moves.extend([(i, amount) for amount in range(1, n + 1)])
        return moves

    def result(self, state, move):
        """Return the new state after making the move."""
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move[0]] -= move[1]
        moves = self.generate_all_moves(board)
        return GameState(
            to_move=("MIN" if state.to_move == "MAX" else "MAX"),
            utility=self.compute_utility(board, move, state.to_move),
            board=board,
            moves=moves,
        )

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return state.utility != 0 or len(state.moves) == 0

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == "MAX" else -state.utility

    def compute_utility(self, board, move, player):
        """If 'MAX' wins with this move, return 1; if 'MIN' wins return -1; else return 0."""
        if sum(board) == 0:
            return 1 if player == "MIN" else -1
        else:
            return 0

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return super().to_move(state)
