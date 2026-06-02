from nnf import And, Or, Var

def nnf_to_dag(formula):

    # Literal
    if isinstance(formula, Var):
        return formula.name if formula.true else f"~{formula.name}"

    # Detecta operador
    if isinstance(formula, And):
        op = "AND"
        same_type = And

    elif isinstance(formula, Or):
        op = "OR"
        same_type = Or

    children_strings = []

    for child in formula.children:

        if isinstance(child, same_type):

            for grandchild in child.children:
                children_strings.append(nnf_to_dag(grandchild))

        else:
            children_strings.append(nnf_to_dag(child))

    return f"({op} " + ", ".join(children_strings) + ")"
    
if __name__ == "__main__":
    A, B, C, D, E = Var("A"), Var("B"), Var("C"), Var("D"), Var("E")

    formula = (A & B) | (C & ~D & E)

    treef = nnf_to_dag(formula)

    print(treef)
    print()

    # ____________________________________________________#

    # Fórmula
    formula2 = (A | B) & C

    print("Fórmula original:")
    print(nnf_to_dag(formula2))

    # Conditioning: A = False
    conditioned = formula2.condition({"A": False})

    print("Após conditioning A: false:")
    print(nnf_to_dag(conditioned))
    print()

    #__________________________________________________#

    # Fórmula
    formula3 = (A & B) | (C & ~D)

    print("Fórmula original:")
    print(nnf_to_dag(formula3))

    # Forget B
    forgotten = formula.forget(["B"])

    print("Após Forget B:")
    print(nnf_to_dag(forgotten))
    print()

    # _________________________________________________________ #

    delta1 = (A | B)
    delta2 = (B | C)

    delta3 = (delta1 & delta2)

    print(f"Delta1 decomposable: {nnf_to_dag(delta1)}")
    print(f"Delta2 decomposable: {nnf_to_dag(delta2)}")
    print(f"Delta3 não decomposable: {nnf_to_dag(delta3)}")
    print(f"Delta3 é deomposable? {delta3.decomposable()}")

    delta4 = delta3.condition({"B": True}) | delta3.condition({"B": False})
    print(f"Delta 4 após Expansão Shannon: {nnf_to_dag(delta4)}")
    print(f"Delta4 é deomposable? {delta4.decomposable()}")
