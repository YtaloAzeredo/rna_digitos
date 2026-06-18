# -*- coding: utf-8 -*-
"""Conjuntos de dados: dígitos cursivos "0" e "1" como grades de pixels 7x5.

'1' = pixel aceso (tinta)   ·   '0' = pixel apagado (fundo)

Convenção de rótulo: alvo 0 -> dígito "0" / alvo 1 -> dígito "1".
Assim, a saída da rede (0 ou 1) é o próprio dígito reconhecido.

As 3 variações de cada dígito simulam diferenças da escrita à mão.
Para usar outros dígitos, basta editar as matrizes abaixo.
"""

# ===========================================================================
# TREINO — 3 exemplos do dígito "0" (anel: borda acesa, centro vazio)
# ===========================================================================
ZERO_1 = ["01110",
          "10001",
          "10001",
          "10001",
          "10001",
          "10001",
          "01110"]

ZERO_2 = ["00110",
          "01001",
          "10001",
          "10001",
          "10001",
          "10010",
          "01100"]

ZERO_3 = ["01110",
          "11011",
          "10001",
          "10001",
          "10001",
          "11011",
          "01110"]

# ===========================================================================
# TREINO — 3 exemplos do dígito "1" (traço vertical central)
# ===========================================================================
UM_1 = ["00100",
        "01100",
        "00100",
        "00100",
        "00100",
        "00100",
        "01110"]

UM_2 = ["00100",
        "01100",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100"]

UM_3 = ["00100",
        "11100",
        "00100",
        "00100",
        "00100",
        "00100",
        "11110"]

# ===========================================================================
# TESTE — variações NÃO vistas no treino (medem a generalização)
# ===========================================================================
TESTE_ZERO_1 = ["01110",
                "10001",
                "10001",
                "11001",   # pequeno ruído/variação
                "10001",
                "10001",
                "01110"]

TESTE_ZERO_2 = ["00110",
                "01001",
                "10001",
                "10001",
                "10001",
                "01001",
                "00110"]

TESTE_UM_1 = ["00100",
              "00100",
              "00100",
              "00100",
              "00100",
              "00100",
              "00100"]   # traço puro, sem bandeira nem base

TESTE_UM_2 = ["00100",
              "01100",
              "00100",
              "00100",
              "00100",
              "00100",
              "11111"]   # base larga


def para_vetor(grade):
    """Achata a grade (lista de strings '0'/'1') em um vetor de inteiros 0/1."""
    vetor = []
    for linha in grade:
        for caractere in linha:
            vetor.append(1 if caractere == "1" else 0)
    return vetor


def conjunto_treino():
    """Lista de (vetor, alvo, nome) com os 3 exemplos de cada dígito."""
    return [
        (para_vetor(ZERO_1), 0, "zero #1"),
        (para_vetor(ZERO_2), 0, "zero #2"),
        (para_vetor(ZERO_3), 0, "zero #3"),
        (para_vetor(UM_1), 1, "um #1"),
        (para_vetor(UM_2), 1, "um #2"),
        (para_vetor(UM_3), 1, "um #3"),
    ]


def conjunto_teste():
    """Lista de (vetor, alvo, nome) com padrões NÃO vistos no treino."""
    return [
        (para_vetor(TESTE_ZERO_1), 0, "zero novo #1"),
        (para_vetor(TESTE_ZERO_2), 0, "zero novo #2"),
        (para_vetor(TESTE_UM_1), 1, "um novo #1"),
        (para_vetor(TESTE_UM_2), 1, "um novo #2"),
    ]
