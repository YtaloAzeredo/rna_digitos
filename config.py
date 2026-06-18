# -*- coding: utf-8 -*-
"""Configurações da RNA Perceptron: dimensões da grade e hiperparâmetros."""

# Dimensões da grade de entrada (cada dígito é uma "imagem" 7x5)
LINHAS = 7
COLUNAS = 5
N_ENTRADAS = LINHAS * COLUNAS  # 35 pixels -> 35 entradas

# Hiperparâmetros do treinamento
TAXA = 0.1          # taxa de aprendizado (η)
MAX_EPOCAS = 100    # limite de épocas (converge em poucas)
