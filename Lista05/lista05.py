from nnf import Var, Or, And
from nnf.dsharp import compile

def mpe(node, weights):

    #Caso Base
    if isinstance(node, Var):
        if node.true:
            prob = weights[node.name]
            assignment = {node.name: True}

        else:
            prob = weights[f"~{node.name}"]
            assignment = {node.name: False}

        return prob, assignment

    #Se for And multiplica
    elif isinstance(node, And):

        total_prob = 1.0
        total_assignment = {}

        for child in node.children:
            prob, assignment = mpe(child, weights)

            total_prob *= prob
            total_assignment.update(assignment)

        return total_prob, total_assignment

    #Se for Or soma
    elif isinstance(node, Or):

        best_prob = -1
        best_assignment = None

        for child in node.children:
            prob, assignment = mpe(child, weights)

            if prob > best_prob:
                best_prob = prob
                best_assignment = assignment

        return best_prob, best_assignment


if __name__ == "__main__":
 
    # Fórmula sd-DNNF: (A ∧ B) ∨ (A ∧ ¬B)
    A = Var("A")
    B = Var("B")
    C = Var("C")

    formula1 = (A & B) | (A & ~B)
    formula2 = (A & B & C) | (A & ~B & C)
    formula3 = (A & B & C) | (~A & B & C)

    # probabilidades
    weights = {
                "A": 0.8,
                "B": 0.9,
                "~B": 0.1,
                "C": 0.7,
                "~A": 0.95
            }
    
    prob1, assignment1 = mpe(formula1, weights)
    prob2, assignment2 = mpe(formula2, weights)
    prob3, assignment3 = mpe(formula3, weights)

    print("MPE probability:", prob1)
    print("Best assignment:", assignment1)

    print("MPE probability:", prob2)
    print("Best assignment:", assignment2)

    print("MPE probability:", prob3)
    print("Best assignment:", assignment3)

    print()
    print("################# questão 3 #######################")
    print()


A, B, C, D, E, F = Var("A"), Var("B"), Var("C"), Var("D"), Var("E"), Var("F")

cnf = And({

    Or({A, B}),

    Or({~A, C}),

    Or({B, C}),

    Or({~B, D}),

    Or({C, D}),

    Or({~C, E}),

    Or({D, E}),

    Or({~D, F}),

    Or({E, F}),

    Or({~E, A})

})

compiled = compile(cnf)
print(compiled)