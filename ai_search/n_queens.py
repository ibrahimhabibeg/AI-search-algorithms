from typing import Iterable
from ai_search.problem import SearchProblem, SearchProblemState, SearchProblemAction
from ai_search.search import HeuristicFunction


class NQueensAction(SearchProblemAction):
    def __init__(self, col: int, new_row: int):
        self.col = col
        self.new_row = new_row

    def get_cost(self) -> float:
        return 1.0  # Each action has a uniform cost


class NQueensState(SearchProblemState):
    def __init__(self, board: list[int], n: int):
        assert len(board) == n
        assert all(0 <= row < n for row in board)
        self.board = board  # board is a list where index is column and value is row
        self.n = n

    def get_actions(self) -> Iterable[SearchProblemAction]:
        for col in range(self.n):
            for row in range(self.n):
                if self.board[col] != row:
                    yield NQueensAction(col, row)

    def __str__(self):
        rows = []
        for r in range(self.n):
            row = []
            for c in range(self.n):
                if self.board[c] == r:
                    row.append("Q")
                else:
                    row.append(".")
            rows.append(" ".join(row))
        return "\n".join(rows)
    
    def __eq__(self, value):
        return isinstance(value, NQueensState) and self.board == value.board

    def __hash__(self):
        return hash(tuple(self.board))


class NQueensProblem(SearchProblem):
    def __init__(self, n: int, initial_state: NQueensState | None = None):
        self.n = n
        self.initial_state = initial_state

    def transition(
        self, state: SearchProblemState, action: SearchProblemAction
    ) -> SearchProblemState:
        new_board = state.board[:]
        new_board[action.col] = action.new_row
        return NQueensState(new_board, self.n)

    def get_initial_state(self) -> SearchProblemState:
        return self.initial_state

    def is_goal(self, state: SearchProblemState) -> bool:
        board = state.board
        n = self.n
        if len(set(board)) < n:
            return False  # Two queens in the same row

        for col1 in range(n):
            for col2 in range(col1 + 1, n):
                if abs(board[col1] - board[col2]) == abs(col1 - col2):
                    return False  # Two queens on the same diagonal
        return True


class NoQueenAttackHeuristic(HeuristicFunction):
    def estimate(self, state: NQueensState) -> float:
        board = state.board
        n = state.n
        attacks = 0

        for col1 in range(n):
            for col2 in range(col1 + 1, n):
                if board[col1] == board[col2] or abs(board[col1] - board[col2]) == abs(
                    col1 - col2
                ):
                    attacks += 1

        return float(attacks)
    
class NoQueenRowAttackHeuristic(HeuristicFunction):
    def estimate(self, state: NQueensState) -> float:
        board = state.board
        n = state.n
        attacks = 0

        for col1 in range(n):
            for col2 in range(col1 + 1, n):
                if board[col1] == board[col2]:
                    attacks += 1

        return float(attacks)
