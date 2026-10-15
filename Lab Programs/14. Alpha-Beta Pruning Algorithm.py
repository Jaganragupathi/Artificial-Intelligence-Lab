
def alphabeta(tree, alpha, beta, maximizing):
    if isinstance(tree, int):
        return tree

    if maximizing:
        value = float("-inf")

        for child in tree:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    value = float("inf")

    for child in tree:
        value = min(value, alphabeta(child, alpha, beta, True))
        beta = min(beta, value)

        if alpha >= beta:
            break

    return value

tree = [[3, 5], [2, 9], [0, 1]]
print("Best value:", alphabeta(tree, float("-inf"), float("inf"), True))
