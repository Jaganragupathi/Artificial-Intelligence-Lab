
regions = ["A", "B", "C", "D"]
colors = ["Red", "Green", "Blue"]

neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

assignment = {}

def solve():
    if len(assignment) == len(regions):
        return True

    region = next(r for r in regions if r not in assignment)

    for color in colors:
        if all(assignment.get(n) != color for n in neighbors[region]):
            assignment[region] = color

            if solve():
                return True

            del assignment[region]

    return False

if solve():
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution")
