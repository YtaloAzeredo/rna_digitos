# rna_digitos

RNA **Perceptron** para reconhecer os dígitos cursivos **"0"** e **"1"**,
implementada do zero em Python (apenas biblioteca padrão), treinada com
**3 exemplos de cada dígito**.

## Como executar

```bash
python3 main.py
```

Não requer instalação de dependências (usa só a biblioteca padrão do Python 3).

## Estrutura dos arquivos

| Arquivo            | Responsabilidade                                            |
|--------------------|-------------------------------------------------------------|
| `config.py`        | Dimensões da grade (7×5) e hiperparâmetros (η, máx. épocas) |
| `dados.py`         | Dígitos "0"/"1" de treino e teste + conversão para vetor    |
| `perceptron.py`    | O modelo, do zero: `predizer` / `treinar` / `avaliar`       |
| `visualizacao.py`  | Arte ASCII: desenho dos dígitos e mapa dos pesos            |
| `main.py`          | Ponto de entrada que orquestra o fluxo                      |

## Ideia

O problema tem apenas 2 classes ("0" e "1"), então **um único perceptron**
(classificador linear binário) é suficiente.

- **Entrada:** cada dígito é uma grade de pixels **7×5 = 35 valores** (0 = fundo,
  1 = tinta), achatada em um vetor de 35 entradas.
- **Rótulo:** `0` para o dígito "0" e `1` para o dígito "1". Logo, a **saída da
  rede (0 ou 1) já é o próprio dígito reconhecido**.
- Os 3 exemplos de cada dígito simulam pequenas variações da escrita à mão.

### Modelo do neurônio

```
saída = degrau( bias + Σ wᵢ·xᵢ )      degrau(s) = 1 se s ≥ 0, senão 0
```

### Regra de aprendizado (Perceptron de Rosenblatt)

Para cada exemplo, com taxa de aprendizado η:

```
erro  = alvo − saída
wᵢ   ← wᵢ   + η · erro · xᵢ
bias ← bias + η · erro
```

Como os dígitos "0" (anel: borda acesa, centro vazio) e "1" (traço vertical
central) são **linearmente separáveis**, o **Teorema da Convergência do
Perceptron** garante que o treino atinge **erro zero** em um número finito de
épocas.

## O que o programa faz

1. Mostra os 6 exemplos de treino em arte ASCII.
2. Treina o perceptron, imprimindo o número de erros por época **até convergir**.
3. Exibe os **pesos aprendidos** como um mapa 7×5 (mostra que a coluna central
   "puxa" para o "1" e as bordas "puxam" para o "0").
4. Avalia no conjunto de treino (espera-se **100%**).
5. Avalia em um **conjunto de teste com padrões não vistos** para demonstrar a
   **generalização**.

## Parâmetros (em `config.py`)

| Parâmetro     | Valor padrão | Descrição                                  |
|---------------|--------------|--------------------------------------------|
| `LINHAS×COLUNAS` | `7×5`     | Dimensões da grade de pixels (35 entradas) |
| `TAXA` (η)    | `0.1`        | Taxa de aprendizado                        |
| `MAX_EPOCAS`  | `100`        | Limite de épocas                           |

Os pesos são inicializados em zero, então a execução é **determinística**
(mesma saída a cada rodada). Para usar outros dígitos, edite as matrizes
`ZERO_1..3` / `UM_1..3` (treino) e `TESTE_*` (teste) em `dados.py`.

## Saída esperada (resumo)

```
TREINAMENTO (regra do perceptron):
      época  1: 2 erro(s)
      época  2: 0 erro(s)
      ==> Convergiu na época 2 (erro zero).
...
AVALIAÇÃO NO CONJUNTO DE TREINO:
      --> Acurácia: 6/6 = 100.0%
...
AVALIAÇÃO NO CONJUNTO DE TESTE (generalização):
      --> Acurácia: 4/4 = 100.0%
```
