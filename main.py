#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RNA Perceptron — Reconhecimento dos dígitos cursivos "0" e "1"
================================================================

Ponto de entrada do programa. Execute com:

    python3 main.py

Estrutura do projeto:
    config.py        -> dimensões da grade e hiperparâmetros
    dados.py         -> dígitos "0"/"1" (treino e teste) + conversão p/ vetor
    perceptron.py    -> o modelo: predizer / treinar / avaliar (do zero)
    visualizacao.py  -> arte ASCII (desenhar dígitos e mapa de pesos)
    main.py          -> orquestra o fluxo (este arquivo)

Como o problema tem apenas 2 classes ("0" e "1"), um ÚNICO perceptron
(classificador linear binário) é suficiente. Os dígitos são linearmente
separáveis, então o Teorema da Convergência garante erro zero no treino.
"""

from config import MAX_EPOCAS
from dados import conjunto_treino, conjunto_teste
from perceptron import treinar, avaliar
from visualizacao import desenhar, visualizar_pesos


def main():
    print("=" * 60)
    print(" RNA PERCEPTRON  —  dígitos cursivos '0' e '1'")
    print("=" * 60)
    print("Entrada: grade 7x5 (35 pixels). Saída 0/1 = dígito reconhecido.\n")

    treino = conjunto_treino()
    teste = conjunto_teste()

    # --- Exemplos de treino ---
    print("-" * 60)
    print("CONJUNTO DE TREINO (3 exemplos de cada dígito):")
    print("-" * 60)
    for x, alvo, nome in treino:
        print(f"\n  {nome}  (rótulo = {alvo}):")
        desenhar(x)

    # --- Treinamento ---
    print("\n" + "-" * 60)
    print("TREINAMENTO (regra do perceptron):")
    print("-" * 60)
    pesos, bias, epoca_conv = treinar(treino)
    if epoca_conv is not None:
        print(f"      ==> Convergiu na época {epoca_conv} (erro zero).")
    else:
        print(f"      ==> NÃO convergiu em {MAX_EPOCAS} épocas.")

    # --- Pesos aprendidos ---
    print("\n" + "-" * 60)
    print("PESOS APRENDIDOS (remodelados em 7x5):")
    print("-" * 60)
    visualizar_pesos(pesos, bias)

    # --- Avaliação no treino ---
    print("\n" + "-" * 60)
    print("AVALIAÇÃO NO CONJUNTO DE TREINO:")
    print("-" * 60)
    avaliar(pesos, bias, treino)

    # --- Conjunto de teste (não visto) ---
    print("-" * 60)
    print("CONJUNTO DE TESTE (padrões NÃO vistos no treino):")
    print("-" * 60)
    for x, alvo, nome in teste:
        print(f"\n  {nome}  (esperado = {alvo}):")
        desenhar(x)

    print("\n" + "-" * 60)
    print("AVALIAÇÃO NO CONJUNTO DE TESTE (generalização):")
    print("-" * 60)
    avaliar(pesos, bias, teste)


if __name__ == "__main__":
    main()
