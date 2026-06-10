from dd.autoref import BDD
# Código que resolve a questão 2

#a) p → q, r → ¬t,q → r |= p → ¬t
bdd_a = BDD()

bdd_a.declare('p', 'q', 'r', 't')

# cláusulas
c1 = bdd_a.add_expr('(~ p) | q')
c2 = bdd_a.add_expr('(~ r) | (~ t)')
c3 = bdd_a.add_expr('(~ q) | r')

# negação da conclusão
c4 = bdd_a.add_expr('p')
c5 = bdd_a.add_expr('t')

formula = c1 & c2 & c3 & c4 & c5

exp = "p → q, r → ¬t,q → r |= p → ¬t"
if formula == bdd_a.false:
    print(f"A expressão {exp} é válida")
else:
    print("Não é consequência lógica")

#b)  (p → q) → r,s → ¬p,t,¬s ∧ t → q |= r
bdd_b = BDD()

bdd_b.declare("p", "q", "r", "s", "t")

#cláusulas
c1 = bdd_b.add_expr("p | q")
c2 = bdd_b.add_expr("(~q) | r")
c3 = bdd_b.add_expr("(~s) | p")
c4 = bdd_b.add_expr("t")
c5 = bdd_b.add_expr("s")
c6 = bdd_b.add_expr("q")
c7 = bdd_b.add_expr("~t")

#negação da conclusão
c8 = bdd_b.add_expr("~r")

formulab = c1 & c2 & c3 & c4 & c5 & c6 & c7 & c8

exp = "(p → q) → r,s → ¬p,t,¬s ∧ t → q |= r"
if formulab == bdd_b.false:
    print(f"A expressão {exp} é válida")
else:
    print("Não é consequência lógica")


#c) (s → p)∨(t → q) |= (s → q)∨(t → p)
bdd_c = BDD()

bdd_c.declare("s", "p", "t", "q")

#Cláusulas
c1 = bdd_c.add_expr("(~s) | p | (~t) | q")

#Negação da conclusão
c2 = bdd_c.add_expr("s")
c3 = bdd_c.add_expr("(~q)")
c4 = bdd_c.add_expr("t")
c5 = bdd_c.add_expr("(~p)")

formulac = c1 & c2 & c3 & c4 & c5

exp = "(s → p)∨(t → q) |= (s → q)∨(t → p)"
if formulac == bdd_c.false:
    print(f"A expressão {exp} é válida")
else:
    print("Não é consequência lógica")


#d) (p ∧ q) → r, r → s,q ∧ ¬s |= ¬p
bdd_d = BDD()

bdd_d.declare("p", "q", "r", "s")

#Cláusulas
c1 = bdd_d.add_expr("(~p) | (~q) | r")
c2 = bdd_d.add_expr("(~r) | s")
c3 = bdd_d.add_expr("q")
c4 = bdd_d.add_expr("(~s)")

#Negação da conclusão
c5 = bdd_d.add_expr("p")

formulad = c1 & c2 & c3 & c4 & c5

exp = "(p ∧ q) → r, r → s,q ∧ ¬s |= ¬p"
if formulad == bdd_d.false:
    print(f"A expressão {exp} é válida")
else:
    print("Não é consequência lógica")
