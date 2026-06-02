# Questão 01a (esse assunto é muito foda!)

1. Uma fórmula sd-DNNF pode ser transformada em um counting graph, onde cada nó OR se torna uma soma (+) e cada nó AND se torna uma multiplicação (*).
2. Dessa forma, a fórmula lógica passa a representar uma função aritmética, permitindo calcular o número de modelos satisfatórios da teoria eficientemente.
3. Cada literal pertencente a S (conj. de evidências) é considerado verdadeiro na fórmula. A função (G(S)) representa o número de modelos compatíveis com as evidências presentes em (S).
4. A derivada parcial: mede quanto o número de modelos quando o literal l é imposto como verdadeiro. Ela indica quantos modelos permanecem válidos quando o literal l é afirmado como verdadeiro.
5. Assertion é a operação de adicionar uma nova evidência ao conjunto S, ou seja, adicionar um novo literal assumido como verdadeiro.
6. Retraction é a operação inversa: remover uma evidência previamente assumida em S, permitindo novamente que o literal possa assumir valores verdadeiro ou falso.
7. As derivadas parciais permitem realizar assertion e retraction eficientemente sem recompilar toda a teoria lógica, apenas propagando valores no counting graph.

# Questão 01b
1. Suponha a fórmula F = (A ∧ B) ∨ (A ∧ ~B)
2. Essa fórmula pode assumir a forma de um counting graph ===> (A * B) + (A * ~B)
3. Suponha S = {}, então G(S) para a fórmula F é: 2.
4. Suponha Assertion A, ou seja, S = {A}, ainda dois modelos possíveis ==> (A=1, B=0), ou seja, G(S) = 2
5. Suponha Assertion B, ou seja, S = {A, B}. Temos que o modelo possível é (A=1, B=1), logo, G(S) = 1
6. Derivada de G em relação a A: B + ~B = 2
7. Derivada de G em relação a B: A = 1

# Questão 03a
1. O c2d se utiliza da caracteristica da decomposabilidade para separar em subfórmulas menores, transformar em d-DNNF e depois unir os resultados com um AND. 
2. Já o DSHARP utiliza técnicas mais atualizadas como: Implicit Binary Constraint Propagation, Conflict Analysis / Non-Chronological Backtracking, 
