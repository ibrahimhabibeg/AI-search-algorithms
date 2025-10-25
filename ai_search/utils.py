from ai_search.problem import SearchNode


def print_path(node: SearchNode):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    for state in reversed(path):
        print(state)
        print()
