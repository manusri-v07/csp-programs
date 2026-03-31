# Simplified Telangana CSP (partial neighbors for demo)

districts = [
    'Adilabad','Nirmal','Mancherial','Nizamabad','Karimnagar',
    'Warangal','Khammam','Nalgonda','Mahbubnagar','Hyderabad'
]

neighbors = {
    'Adilabad': ['Nirmal'],
    'Nirmal': ['Adilabad','Nizamabad'],
    'Mancherial': ['Karimnagar'],
    'Nizamabad': ['Nirmal','Karimnagar'],
    'Karimnagar': ['Nizamabad','Warangal'],
    'Warangal': ['Karimnagar','Khammam'],
    'Khammam': ['Warangal','Nalgonda'],
    'Nalgonda': ['Khammam','Hyderabad'],
    'Hyderabad': ['Nalgonda','Mahbubnagar'],
    'Mahbubnagar': ['Hyderabad']
}

colors = ['Red','Green','Blue','Yellow']

def is_safe(district, color, assignment):
    for n in neighbors.get(district, []):
        if n in assignment and assignment[n] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    for d in districts:
        if d not in assignment:
            for c in colors:
                if is_safe(d, c, assignment):
                    assignment[d] = c
                    result = backtrack(assignment)
                    if result:
                        return result
                    del assignment[d]
            return None

solution = backtrack({})
print("Telangana Coloring:")
for d, c in solution.items():
    print(d, "->", c)