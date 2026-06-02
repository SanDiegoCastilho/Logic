from nnf import And, Or, Var


from nnf import Var, And, Or

def min_false_cardinality(node):

    # literal
    if isinstance(node, Var):

        # literal negado
        if node.true is False:
            return 1

        # literal positivo
        return 0

    # OR
    elif isinstance(node, Or):

        return min(min_false_cardinality(child) for child in node.children)

    # AND
    elif isinstance(node, And):

        return sum( min_false_cardinality(child) for child in node.children)

    else:
        raise TypeError("Nó não reconhecido na fórmula")


if __name__ == '__main__':
##################################################
#   QUESTÃO 01
##################################################

    #Fórmulas base
    a1, b1, c1, d1 = Var('a1'), Var('b1'), Var('c1'), Var('d1')
    e2, f2, g2, h2 = Var('e2'), Var('f2'), Var('g2'), Var('h2')
    i3, j3, k3, l3 = Var('i3'), Var('j3'), Var('k3'), Var('l3')

    D1 = (a1 & b1) | (c1 & d1)
    D2 = (D1 & (e2 |f2)) | (g2 & h2)
    D3 = (D2 & (i3 | j3)) | (k3 & l3)

    #Fórmula alvo que quero provar
    target = a1 | c1 | g2 | k3

    #Se for INSAT é pq a fórmula D3 |= target é válido
    formula = D3  & target.negate()

    model = formula.solve()

    if model is None:
        print("D3 satisfaz a fórmula")
        print(f"D3 |= {target}")

    else:
        print("A implicação não vale")
        print("Contraexemplo: \n")

        for var, valor in model.items():
            print(f"{var.name} = {valor}")

    print()
##################################################
#   QUESTÃO 02 - Estou supondo que que s-DNNF tem Determinismo
##################################################
    print("############################ Questão 2 ##########################################")
    a, b, c, d, e, f = Var('a'), Var('b'), Var('c'), Var('d'), Var('e'), Var('f')
    g, h, i, j, k, l = Var('g'), Var('h'), Var('i'), Var('j'), Var('k'), Var('l')

    Delta = ((a & ~b) | (~a & b)) & ((c & ~d) | (~c & d)) & ((e & ~f) | (~e & f)) & g & h & i & ~j & k & ~l

    min_false = min_false_cardinality(Delta)

    print(f"A quantidade mínima de falses para satisfazer a formula é: {min_false}")

    ## Resposta item 3: Se tirar smoothness, esse algoritmo ainda funciona? Justifique a sua resposta?
    ## Pelo o que eu entendi, sim, continua funcionando. Por que o algoritmo só depende de determinismo e decomposable,
    ## o smoothness não interfere nesse caso.

    ## Item 4: infelizmente faltei aula eu tô apanhando aqui para saber qual foi o algoritmo