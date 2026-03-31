# Map Coloring using CSP (Backtracking)

states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Adjacency list
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

def is_safe(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment

    for state in states:
        if state not in assignment:
            for color in colors:
                if is_safe(state, color, assignment):
                    assignment[state] = color
                    result = backtrack(assignment)
                    if result:
                        return result
                    del assignment[state]
            return None

solution = backtrack({})
print("Australia Map Coloring Solution:")
for state, color in solution.items():
    print(state, "->", color)