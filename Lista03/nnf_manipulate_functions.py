from graphviz import Digraph
from nnf import Var, And, Or
from pathlib import Path
import itertools

# ==================================================
# Configuração
# ==================================================

OUTPUT_DIR = Path("Lista03/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

counter = itertools.count()

# ==================================================
# DAG Builder
# ==================================================

counter = itertools.count()


def reset_counter():
    global counter
    counter = itertools.count()


def flatten(node, op_type):
    result = []

    for child in node.children:
        if isinstance(child, op_type):
            result.extend(flatten(child, op_type))
        else:
            result.append(child)

    return result


def nnf_to_dag(formula, dag, flat=False):
    node_id = f"n{next(counter)}"

    # Literal
    if isinstance(formula, Var):
        label = formula.name if formula.true else f"¬{formula.name}"
        dag.node(node_id, label)
        return node_id

    

    # AND
    if isinstance(formula, And):
        if formula.size() == 0:
            dag.node(node_id, f"{formula}")

        else:
            dag.node(node_id, "AND")

            children = (flatten(formula, And) if flat else formula.children)

            for child in children:
                child_id = nnf_to_dag(child, dag, flat)
                dag.edge(node_id, child_id)

        return node_id

    # OR
    if isinstance(formula, Or):
        if formula.size() == 0:
            dag.node(node_id, f"{formula}")

        else:
            dag.node(node_id, "OR")

            children = (flatten(formula, Or) if flat else formula.children)

            for child in children:
            
                child_id = nnf_to_dag(child, dag, flat)
                dag.edge(node_id, child_id)

        return node_id
    


    raise TypeError(f"Tipo não suportado: {type(formula)}")

# ==================================================
# Renderização
# ==================================================

def render_formula(formula, filename, flat=False):
    reset_counter()

    dag = Digraph(filename)

    nnf_to_dag(formula, dag, flat)

    path = OUTPUT_DIR / filename

    dag.render(str(path), format="png", cleanup=True)

    print(f"[OK] {filename}.png")

# ==================================================
# Utilidades de Experimento
# ==================================================

def show_decomposable(name, formula):
    print(f"{name}: decomposable = {formula.decomposable()}")

def shannon_expansion(formula, variable):
    return (formula.condition({variable: True}) | formula.condition({variable: False}))