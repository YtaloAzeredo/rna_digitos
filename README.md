# rna_digitos

RNA **Perceptron** para reconhecer os dígitos cursivos **"0"** e **"1"**,
implementada do zero em Python (apenas biblioteca padrão), treinada com
**2 exemplos de cada dígito**.

## Como executar

O projeto usa só a biblioteca padrão do Python: **não há dependências para
instalar** nem ambiente virtual para criar.

### Pré-requisitos

- **Python 3.6 ou superior**
- **Git** (opcional, apenas para clonar o repositório)

### Passo a passo

**1. Verifique se o Python está instalado**

```bash
python3 --version
```

Deve aparecer algo como `Python 3.9.6`. No Windows, o comando costuma ser
`python` (ou `py`) em vez de `python3`. Se não estiver instalado, baixe em
<https://www.python.org/downloads/>.

**2. Obtenha o código**

Clonando com o Git:

```bash
git clone https://github.com/YtaloAzeredo/rna_digitos.git
```

Ou, sem o Git, baixe o ZIP pelo GitHub (**Code → Download ZIP**) e extraia.

**3. Entre na pasta do projeto**

```bash
cd rna_digitos
```

O programa precisa ser executado de dentro desta pasta, pois `main.py` importa
os outros arquivos (`config.py`, `dados.py`, `perceptron.py`,
`visualizacao.py`) do mesmo diretório.

**4. Execute o programa**

```bash
python3 main.py
```

No Windows: `python main.py`.

**5. Confira o resultado**

O terminal mostra, em ordem: os dígitos de treino, os erros por época até a
convergência, o mapa dos pesos aprendidos e a acurácia no treino e no teste.
O resultado deve bater com a seção [Saída esperada](#saída-esperada-resumo).

### Problemas comuns

- **Os símbolos `█`, `·`, `✓` aparecem trocados ou ocorre `UnicodeEncodeError`
  (Windows):** o terminal não está em UTF-8. Execute `chcp 65001` antes, ou
  rode com `python -X utf8 main.py`.
- **`ModuleNotFoundError: No module named 'config'`:** o programa foi executado
  de fora da pasta do projeto. Volte ao passo 3.

### Alterando os dígitos ou os parâmetros (opcional)

1. Edite as matrizes de treino e teste em `dados.py` (cada dígito é uma lista
   de 3 strings com 3 caracteres: `1` = pixel aceso, `0` = apagado).
2. Se quiser, ajuste a taxa de aprendizado e o limite de épocas em `config.py`.
3. Execute `python3 main.py` novamente para ver o novo resultado.

## Estrutura dos arquivos

| Arquivo            | Responsabilidade                                            |
|--------------------|-------------------------------------------------------------|
| `config.py`        | Dimensões da grade (3×3) e hiperparâmetros (η, máx. épocas) |
| `dados.py`         | Dígitos "0"/"1" de treino e teste + conversão para vetor    |
| `perceptron.py`    | O modelo, do zero: `predizer` / `treinar` / `avaliar`       |
| `visualizacao.py`  | Arte ASCII: desenho dos dígitos e mapa dos pesos            |
| `main.py`          | Ponto de entrada que orquestra o fluxo                      |

## Ideia

O problema tem apenas 2 classes ("0" e "1"), então **um único perceptron**
(classificador linear binário) é suficiente.

- **Entrada:** cada dígito é uma grade de pixels **3×3 = 9 valores** (0 = fundo,
  1 = tinta), achatada em um vetor de 9 entradas.
- **Rótulo:** `0` para o dígito "0" e `1` para o dígito "1". Logo, a **saída da
  rede (0 ou 1) já é o próprio dígito reconhecido**.
- Os 2 exemplos de cada dígito simulam pequenas variações da escrita à mão.

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

1. Mostra os 4 exemplos de treino em arte ASCII.
2. Treina o perceptron **até convergir**, imprimindo o passo a passo de cada
   exemplo (soma, saída, erro e pesos corrigidos) e os erros por época.
3. Exibe os **pesos aprendidos** como um mapa 3×3 (mostra que a coluna central
   "puxa" para o "1" e as laterais "puxam" para o "0").
4. Avalia no conjunto de treino (espera-se **100%**), mostrando a soma de cada
   exemplo.
5. Avalia em um **conjunto de teste com padrões não vistos** (1 de cada
   dígito) para demonstrar a **generalização**.

## Parâmetros (em `config.py`)

| Parâmetro     | Valor padrão | Descrição                                  |
|---------------|--------------|--------------------------------------------|
| `LINHAS×COLUNAS` | `3×3`     | Dimensões da grade de pixels (9 entradas)  |
| `TAXA` (η)    | `0.1`        | Taxa de aprendizado                        |
| `MAX_EPOCAS`  | `100`        | Limite de épocas                           |

Os pesos são inicializados em zero, então a execução é **determinística**
(mesma saída a cada rodada). Para usar outros dígitos, edite as matrizes
`ZERO_1..2` / `UM_1..2` (treino) e `TESTE_ZERO` / `TESTE_UM` (teste) em `dados.py`.

## Saída esperada (resumo)

O treino mostra, para cada exemplo, a soma ponderada, a saída da rede e, quando
ela erra, os pesos e o bias já corrigidos:

```
TREINAMENTO (regra do perceptron):
      Início: todos os pesos = 0 e bias = 0   (η = 0.1)

      ÉPOCA 1
        zero #1  soma = +0.00 -> saída 1 (alvo 0)  ERROU (erro = -1)
                 diminui os pesos dos pixels acesos:
                 pesos = [-0.10 -0.10 -0.10 -0.10 +0.00 -0.10 -0.10 -0.10 -0.10]
                 bias  = -0.10
        zero #2  soma = -0.70 -> saída 0 (alvo 0)  acertou, pesos mantidos
        ...
        => 3 erro(s) nesta época

      ÉPOCA 2
        ...
        => 1 erro(s) nesta época

      ÉPOCA 3
        ...
        => 0 erro(s) nesta época
      ==> Convergiu na época 3 (erro zero).
...
AVALIAÇÃO NO CONJUNTO DE TREINO:
      ✓ zero #1    soma = -0.90  ->  previsto = 0   esperado = 0
      ✓ zero #2    soma = -0.50  ->  previsto = 0   esperado = 0
      ✓ um #1      soma = +0.10  ->  previsto = 1   esperado = 1
      ✓ um #2      soma = +0.00  ->  previsto = 1   esperado = 1
      --> Acurácia: 4/4 = 100.0%
...
AVALIAÇÃO NO CONJUNTO DE TESTE (generalização):
      ✓ zero novo  soma = -0.70  ->  previsto = 0   esperado = 0
      ✓ um novo    soma = +0.20  ->  previsto = 1   esperado = 1
      --> Acurácia: 2/2 = 100.0%
```
