from nnf_manipulate_functions import *

def exercise_2():
    print("\n=== Exercício 2 ===")
    print(" [Resposta] Acredito ser impossível de achar uma fórmula não decomposable, soothness e deterministc " \
            "que não exista uma outra fórmula equivalente que tenha essas 3 caracteristicas ")

def exercise_5a(A, B, C):
    print("\n=== Exercício 5a: Conditioning ===")

    formula = (A | B) & C
    print(f"Fórmula original = {formula}")

    render_formula(formula,"formula-nnf-5a-original", flat=True)

    conditioned = formula.condition({"A": False})
    print(f"Fórmula condicionada com A False = {conditioned}")

    render_formula(conditioned,"formula-nnf-5a-conditioned")

def exercise_5b(A, B, C, D):
    print("\n=== Exercício 5b: Forget ===")

    formula = (A & B) | (C & ~D)

    render_formula(formula, "formula-nnf-5b-original")

    forgotten = formula.forget(["B"])

    render_formula(forgotten,"formula-nnf-5b-forgotten")

def exercise_6ab(A, B, C):
    print("\n=== Exercício 4 ===")

    delta1 = (A | B)
    delta2 = (B | C)

    delta3 = delta1 & delta2

    render_formula(delta1, "delta1")
    render_formula(delta2, "delta2")
    render_formula(delta3, "delta3")

    show_decomposable("delta1", delta1)
    show_decomposable("delta2", delta2)
    show_decomposable("delta3", delta3)

    delta4 = shannon_expansion(delta3, "B")

    render_formula(delta4, "delta4-shannon")

    show_decomposable("delta4", delta4)

        
if __name__ == "__main__":
    A = Var("A")
    B = Var("B")
    C = Var("C")
    D = Var("D")
    E = Var("E")

    exercise_2()
    exercise_5a(A, B, C)
    exercise_5b(A, B, C, D)
    exercise_6ab(A, B, C)
