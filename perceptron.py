# -*- coding: utf-8 -*-
"""Perceptron implementado do zero: modelo, treino e avaliação.

Modelo do neurônio:
    saída = degrau( bias + Σ wᵢ·xᵢ )      degrau(s) = 1 se s >= 0, senão 0

Regra de aprendizado (Perceptron de Rosenblatt):
    erro  = alvo − saída
    wᵢ   += η · erro · xᵢ
    bias += η · erro
"""

from config import N_ENTRADAS, TAXA, MAX_EPOCAS


def predizer(pesos, bias, x):
    """Soma ponderada + função degrau (Heaviside). Retorna 0 ou 1."""
    soma = bias
    for i in range(len(x)):
        soma += pesos[i] * x[i]
    return 1 if soma >= 0 else 0


def treinar(dados, taxa=TAXA, max_epocas=MAX_EPOCAS, verbose=True):
    """Treina o perceptron pela regra de aprendizado de Rosenblatt.

    `dados` é uma lista de tuplas (x, alvo, nome).
    Retorna (pesos, bias, epoca_convergencia).
    """
    pesos = [0.0] * N_ENTRADAS   # inicialização determinística (zeros)
    bias = 0.0
    epoca_conv = None

    for epoca in range(1, max_epocas + 1):
        erros = 0
        for x, alvo, _ in dados:
            saida = predizer(pesos, bias, x)
            erro = alvo - saida
            if erro != 0:
                for i in range(N_ENTRADAS):
                    pesos[i] += taxa * erro * x[i]
                bias += taxa * erro
                erros += 1
        if verbose:
            print(f"      época {epoca:>2}: {erros} erro(s)")
        if erros == 0:
            epoca_conv = epoca
            break

    return pesos, bias, epoca_conv


def avaliar(pesos, bias, conjunto, titulo=""):
    """Classifica cada exemplo do conjunto e imprime a acurácia.

    Retorna (acertos, total).
    """
    print(titulo)
    acertos = 0
    for x, alvo, nome in conjunto:
        previsto = predizer(pesos, bias, x)
        ok = previsto == alvo
        acertos += 1 if ok else 0
        marca = "✓" if ok else "✗"
        print(f"      {marca} {nome:<14} esperado={alvo}  previsto={previsto}")
    total = len(conjunto)
    pct = 100.0 * acertos / total if total else 0.0
    print(f"      --> Acurácia: {acertos}/{total} = {pct:.1f}%\n")
    return acertos, total
