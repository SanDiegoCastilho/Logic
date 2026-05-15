# Logic
Lista 03 Tópicos em Lógica

Questões 1 e 3
Bova, Capelli, Mengel e Slivovsky provaram que existem fórmulas que conseguem ser escritas de forma compacta no formato PI, mas que quando você tenta converter para o formato DNNF, a representação explode exponencialmente de tamanho. A função testemunha usada é baseada em grafos que tem uma descrição PI pequena, mas não tem jeito de representar em DNNF sem crescer exponencialmente.. (https://arxiv.org/pdf/1411.1995)

Bova usa uma função de Sauerhoff,  uma função sobre matrizes n×n de variáveis boolenas,  para provar uma separação exponencial de DNNF em relação a d-DNNF (deterministic DNNF). Isso foi obtido conectando compilação de conhecimento a técnicas de communication complexity. (https://www.ijcai.org/Proceedings/16/Papers/147.pdf)

Trabalhos posteriores confirmaram que d-DNNF suporta em polytime as verificações de consistência (CO), validade (VA), entailment clausal (CE), implicant (IM), contagem de modelos (CT) e enumeração de modelos (ME) (https://arxiv.org/pdf/2603.09975v2)

Questão 02
Decomposable: (A v B v C) ^ (B v D v E)
Deterministic: (~A ^ B) v (D ^ C)
Smoothness: (A ^ B) v (C ^ D)
