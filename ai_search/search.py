from abc import ABC, abstractmethod
from ai_search.problem import SearchProblem, SearchProblemState, SearchNode
from queue import PriorityQueue


class BestFirstSearchFunction(ABC):
    @abstractmethod
    def evaluate(self, node: SearchNode) -> float:
        """Evaluate the given search node and return a numeric value for prioritization."""
        pass


def best_first_search(
    problem: SearchProblem,
    search_function: BestFirstSearchFunction,
) -> tuple[SearchNode | None, int]:
    """Perform best-first search on the given problem using the provided search function."""

    root_node = SearchNode(state=problem.get_initial_state(), path_cost=0)
    frontier: PriorityQueue[tuple[float, int, SearchNode]] = PriorityQueue()
    frontier.put((search_function.evaluate(root_node), 0, root_node))
    explored: dict[SearchProblemState, SearchNode] = {}

    no_explored = 0
    no_frontier_updates = 0

    while frontier.qsize() > 0:
        _, _, current_node = frontier.get()
        no_explored += 1

        if problem.is_goal(current_node.state):
            return current_node, no_explored

        explored[current_node.state] = current_node

        for action in current_node.state.get_actions():
            child_node = SearchNode(
                state=problem.transition(current_node.state, action),
                parent=current_node,
                action=action,
                path_cost=current_node.path_cost + action.get_cost(),
            )

            if (
                child_node.state not in explored
                or child_node.path_cost < explored[child_node.state].path_cost
            ):
                no_frontier_updates += 1
                frontier.put(
                    (
                        search_function.evaluate(child_node),
                        no_frontier_updates,
                        child_node,
                    )
                )
                explored[child_node.state] = child_node

    return None, no_explored


class UniformCostSearchFunction(BestFirstSearchFunction):
    def evaluate(self, node: SearchNode) -> float:
        """Evaluate the node based on its path cost for uniform-cost search."""
        return node.path_cost


def uniform_cost_search(problem: SearchProblem) -> tuple[SearchNode | None, int]:
    """Perform uniform-cost search on the given problem."""
    return best_first_search(problem, UniformCostSearchFunction())


class HeuristicFunction(ABC):
    @abstractmethod
    def estimate(self, state: SearchProblemState) -> float:
        """Estimate the cost from the given state to the nearest goal."""
        pass


class AStarSearchFunction(BestFirstSearchFunction):
    def __init__(self, heuristic: HeuristicFunction):
        self.heuristic = heuristic

    def evaluate(self, node: SearchNode) -> float:
        """Evaluate the node based on its path cost and heuristic estimate for A* search."""
        return node.path_cost + self.heuristic.estimate(node.state)


def a_star_search(
    problem: SearchProblem, heuristic: HeuristicFunction
) -> tuple[SearchNode | None, int]:
    """Perform A* search on the given problem using the provided heuristic."""
    return best_first_search(problem, AStarSearchFunction(heuristic))
