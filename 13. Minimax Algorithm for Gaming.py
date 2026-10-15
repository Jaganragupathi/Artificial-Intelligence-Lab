
def minimax(tree, maximizing):
    if isinstance(tree, int):
        return tree

    values = [minimax(child, not maximizing) for child in tree]

    if maximizing:
        return max(values)

    return min(values)

tree = [[3, 5], [2, 9], [0, 1]]
print("Best value:", minimax(tree, True))
