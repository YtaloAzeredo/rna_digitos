# -*- coding: utf-8 -*-
"""Conjuntos de dados: dígitos cursivos "0" e "1" como grades de pixels 3x3.

'1' = pixel aceso (tinta)   ·   '0' = pixel apagado (fundo)

Convenção de rótulo: alvo 0 -> dígito "0" / alvo 1 -> dígito "1".
Assim, a saída da rede (0 ou 1) é o próprio dígito reconhecido.

As 2 variações de cada dígito simulam diferenças da escrita à mão.
Para usar outros dígitos, basta editar as matrizes abaixo.
"""

# ===========================================================================
# TREINO — 2 exemplos do dígito "0" (anel: borda acesa, centro vazio)
# ===========================================================================
ZERO_1 = ["111",
          "101",
          "111"]

ZERO_2 = ["010",   # cantos superiores abertos
          "101",
          "111"]

# ===========================================================================
# TREINO — 2 exemplos do dígito "1" (traço vertical central)
# ===========================================================================
UM_1 = ["010",
        "110",   # traço lateral no meio
        "010"]

UM_2 = ["010",
        "010",
        "111"]   # com base

# ===========================================================================
# TESTE — 1 exemplo de cada dígito, NÃO visto no treino (mede a generalização)
# ===========================================================================
TESTE_ZERO = ["111",
              "101",
              "010"]   # cantos inferiores abertos

TESTE_UM = ["010",
            "010",
            "010"]   # traço puro, sem base


def para_vetor(grade):
    """Achata a grade (lista de strings '0'/'1') em um vetor de inteiros 0/1."""
    vetor = []
    for linha in grade:
        for caractere in linha:
            vetor.append(1 if caractere == "1" else 0)
    return vetor


def conjunto_treino():
    """Lista de (vetor, alvo, nome) com os 2 exemplos de cada dígito."""
    return [
        (para_vetor(ZERO_1), 0, "zero #1"),
        (para_vetor(ZERO_2), 0, "zero #2"),
        (para_vetor(UM_1), 1, "um #1"),
        (para_vetor(UM_2), 1, "um #2"),
    ]


def conjunto_teste():
    """Lista de (vetor, alvo, nome) com padrões NÃO vistos no treino."""
    return [
        (para_vetor(TESTE_ZERO), 0, "zero novo"),
        (para_vetor(TESTE_UM), 1, "um novo"),
    ]
