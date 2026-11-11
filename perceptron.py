# -*- coding: utf-8 -*-
"""Perceptron implementado do zero: modelo, treino e teste.

O perceptron é um único neurônio artificial. Ele "pensa" em dois passos:

    1) soma  = bias + Σ wᵢ·xᵢ            (soma ponderada das entradas)
    2) saída = 1 se soma >= 0, senão 0   (função degrau)

E "aprende" corrigindo os pesos sempre que erra (regra de Rosenblatt):

    erro  = alvo − saída                 (+1, −1 ou 0)
    wᵢ   += η · erro · xᵢ                (só mudam os pesos dos pixels acesos)
    bias += η · erro

Leitura sugerida: `predizer` (como a rede decide) -> `treinar` (como ela
aprende) -> `avaliar` (como medimos se aprendeu).
"""

from config import N_ENTRADAS, TAXA, MAX_EPOCAS

RECUO = "      "   # alinhamento das mensagens impressas no terminal


# ===========================================================================
# 1. O NEURÔNIO — como a rede decide
# ===========================================================================
def soma_ponderada(pesos, bias, x):
    """Passo 1: bias + Σ wᵢ·xᵢ.

    Como cada entrada xᵢ vale 0 ou 1, isto equivale a somar o bias com os
    pesos dos pixels ACESOS do dígito.
    """
    soma = bias
    for peso, entrada in zip(pesos, x):
        soma += peso * entrada
    return soma


def degrau(soma):
    """Passo 2: função de ativação degrau. Retorna 1 se soma >= 0, senão 0."""
    return 1 if soma >= 0 else 0


def predizer(pesos, bias, x):
    """Classifica um dígito: devolve 0 ou 1 (o próprio dígito reconhecido)."""
    return degrau(soma_ponderada(pesos, bias, x))


# ===========================================================================
# 2. O TREINO — como a rede aprende
# ===========================================================================
def corrigir(pesos, bias, x, erro, taxa):
    """Aplica a regra de Rosenblatt e devolve os novos (pesos, bias).

    erro = +1 -> a rede disse "0" mas era "1": AUMENTA os pesos dos pixels acesos.
    erro = −1 -> a rede disse "1" mas era "0": DIMINUI os pesos dos pixels acesos.
    Pixels apagados (xᵢ = 0) não alteram o seu peso.
    """
    novos_pesos = [peso + taxa * erro * entrada
                   for peso, entrada in zip(pesos, x)]
    novo_bias = bias + taxa * erro
    return novos_pesos, novo_bias


def treinar(dados, taxa=TAXA, max_epocas=MAX_EPOCAS, verbose=True):
    """Treina o perceptron até acertar todos os exemplos (ou esgotar as épocas).

    `dados` é uma lista de tuplas (x, alvo, nome).
    Retorna (pesos, bias, epoca_convergencia); a época é None se não convergiu.

    Uma ÉPOCA é uma passada completa pelos exemplos de treino. O treino
    termina na primeira época em que nenhum exemplo é classificado errado.
    """
    # Ponto de partida: a rede não sabe nada (tudo zero -> execução determinística).
    pesos = [0.0] * N_ENTRADAS
    bias = 0.0

    if verbose:
        print(f"{RECUO}Início: todos os pesos = 0 e bias = 0   (η = {taxa})")

    for epoca in range(1, max_epocas + 1):
        if verbose:
            print(f"\n{RECUO}ÉPOCA {epoca}")
        erros_na_epoca = 0

        for x, alvo, nome in dados:
            # 1) A rede tenta classificar o exemplo com os pesos atuais.
            soma = soma_ponderada(pesos, bias, x)
            saida = degrau(soma)

            # 2) Compara com a resposta certa.
            erro = alvo - saida

            # 3) Se errou, corrige os pesos; se acertou, não mexe em nada.
            if erro != 0:
                pesos, bias = corrigir(pesos, bias, x, erro, taxa)
                erros_na_epoca += 1

            if verbose:
                _mostrar_passo(nome, soma, saida, alvo, erro, pesos, bias)

        if verbose:
            print(f"{RECUO}  => {erros_na_epoca} erro(s) nesta época")

        # Critério de parada: uma época inteira sem nenhum erro.
        if erros_na_epoca == 0:
            return pesos, bias, epoca

    return pesos, bias, None   # esgotou as épocas sem convergir


# ===========================================================================
# 3. O TESTE — como medimos se a rede aprendeu
# ===========================================================================
def avaliar(pesos, bias, conjunto):
    """Classifica cada exemplo com os pesos já treinados e imprime a acurácia.

    Aqui a rede NÃO aprende: os pesos ficam fixos, só conferimos as respostas.
    Retorna (acertos, total).
    """
    acertos = 0
    for x, alvo, nome in conjunto:
        soma = soma_ponderada(pesos, bias, x)
        previsto = degrau(soma)
        acertou = previsto == alvo
        if acertou:
            acertos += 1
        marca = "✓" if acertou else "✗"
        print(f"{RECUO}{marca} {nome:<10} soma = {_num(soma)}  ->  "
              f"previsto = {previsto}   esperado = {alvo}")

    total = len(conjunto)
    porcentagem = 100.0 * acertos / total if total else 0.0
    print(f"{RECUO}--> Acurácia: {acertos}/{total} = {porcentagem:.1f}%\n")
    return acertos, total


# ===========================================================================
# Auxiliares de impressão (não fazem parte do algoritmo)
# ===========================================================================
def _num(valor):
    """Formata um número com sinal e 2 casas, sem exibir '-0.00'."""
    texto = f"{valor:+.2f}"
    return "+0.00" if texto == "-0.00" else texto


def _mostrar_passo(nome, soma, saida, alvo, erro, pesos, bias):
    """Imprime o que aconteceu com um exemplo durante o treino."""
    print(f"{RECUO}  {nome:<8} soma = {_num(soma)} -> saída {saida} "
          f"(alvo {alvo})  ", end="")
    if erro == 0:
        print("acertou, pesos mantidos")
    else:
        sentido = "aumenta" if erro > 0 else "diminui"
        print(f"ERROU (erro = {erro:+d})")
        lista = " ".join(_num(peso) for peso in pesos)
        print(f"{RECUO}           {sentido} os pesos dos pixels acesos:")
        print(f"{RECUO}           pesos = [{lista}]")
        print(f"{RECUO}           bias  = {_num(bias)}")
