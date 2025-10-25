from typing import Iterable, Self
from abc import ABC, abstractmethod


class SearchProblemAction(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        """Return the cost associated with this action."""
        pass


class SearchProblemState(ABC):
    @abstractmethod
    def get_actions(self) -> Iterable[SearchProblemAction]:
        """Return a list of possible actions from this state."""
        pass


class SearchProblem(ABC):
    @abstractmethod
    def is_goal(self, state: SearchProblemState) -> bool:
        """Check if the given state is a goal state."""
        pass

    @abstractmethod
    def transition(
        self, state: SearchProblemState, action: SearchProblemAction
    ) -> SearchProblemState:
        """Return the new state after applying the action to the given state."""
        pass

    @abstractmethod
    def get_initial_state(self) -> SearchProblemState:
        """Return the initial state of the search problem."""
        pass


class SearchNode:
    def __init__(
        self,
        state: SearchProblemState,
        parent: Self | None = None,
        action: SearchProblemAction | None = None,
        path_cost: float = 0.0,
    ):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
