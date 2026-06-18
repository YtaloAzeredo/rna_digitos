# -*- coding: utf-8 -*-
"""Visualização em arte ASCII: desenho dos dígitos e mapa dos pesos."""

from config import LINHAS, COLUNAS


def desenhar(vetor):
    """Imprime o padrão como arte ASCII (█ = aceso, · = apagado)."""
    for i in range(LINHAS):
        linha = "".join("█" if vetor[i * COLUNAS + j] == 1 else "·"
                        for j in range(COLUNAS))
        print("      " + linha)


def visualizar_pesos(pesos, bias):
    """Mostra o 'mapa' dos pesos remodelado em 7x5.

    '#' peso forte positivo (puxa p/ "1")  ·  '+' positivo fraco
    '=' peso forte negativo (puxa p/ "0")  ·  '-' negativo fraco  ·  ' ' ~zero
    """
    maxabs = max((abs(w) for w in pesos), default=1.0) or 1.0
    print(f"      (bias = {bias:+.2f})")
    print("      legenda: # ++ forte→'1'   = -- forte→'0'   espaço ~0")
    for i in range(LINHAS):
        linha = ""
        for j in range(COLUNAS):
            r = pesos[i * COLUNAS + j] / maxabs
            if r >= 0.5:
                s = "#"
            elif r > 0.1:
                s = "+"
            elif r <= -0.5:
                s = "="
            elif r < -0.1:
                s = "-"
            else:
                s = " "
            linha += s
        print("      |" + linha + "|")
