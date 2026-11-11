# -*- coding: utf-8 -*-
"""Configurações da RNA Perceptron: dimensões da grade e hiperparâmetros."""

# Dimensões da grade de entrada (cada dígito é uma "imagem" 3x3)
LINHAS = 3
COLUNAS = 3
N_ENTRADAS = LINHAS * COLUNAS  # 9 pixels -> 9 entradas

# Hiperparâmetros do treinamento
TAXA = 0.1          # taxa de aprendizado (η)
MAX_EPOCAS = 100    # limite de épocas (converge em poucas)
