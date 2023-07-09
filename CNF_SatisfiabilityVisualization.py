import matplotlib.pyplot as plt

def visualize_cnf_satisfiability(formula, assignment=None):
    num_clauses = len(formula)
    num_variables = max(abs(literal) for clause in formula for literal in clause)
    
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlim([-1, num_variables + 1])
    ax.set_ylim([-1, num_clauses + 1])
    ax.set_aspect('equal')

    # Plotting clauses
    for i, clause in enumerate(formula):
        y = num_clauses - i
        for literal in clause:
            x = abs(literal)
            color = 'black'
            if assignment is not None:
                if (literal > 0 and assignment[abs(literal)]) or (literal < 0 and not assignment[abs(literal)]):
                    color = 'green'
                else:
                    color = 'red'
            ax.text(x, y, str(literal), color=color, ha='center', va='center')

    # Plotting variable labels
    for i in range(1, num_variables + 1):
        ax.text(i, num_clauses + 0.5, f'x{i}', ha='center', va='center')

    ax.axis('off')
    plt.show()


# Example usage
formula = [[1, 2, -3], [-1, -2, 4], [3, 4]]
assignment = {1: True, 2: False, 3: False, 4: True}

visualize_cnf_satisfiability(formula, assignment)
