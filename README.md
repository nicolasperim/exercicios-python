# 🐍 Exercícios de Lógica e Fundamentos em Python

Repositório criado para registrar minha evolução nos fundamentos de programação e lógica com Python, aplicando boas práticas de código (Clean Code), modularização com funções e manipulação de estruturas de dados.

## 📌 Desafios Concluídos

### 1. Verificador de Paridade (`Python/desafio1.py`)
* **Conceito:** Separação da regra de negócio (função) da interface do usuário.
* **Destaque:** Uso de retornos booleanos (`True`/`False`) em vez de mensagens diretas, tornando a função reutilizável.

### 2. Calculadora de Média Escolar (`Python/desafio2.py`)
* **Conceito:** Passagem de listas como parâmetros em funções.
* **Destaque:** Implementação dinâmica utilizando `sum()` e `len()`, permitindo calcular médias para qualquer quantidade de notas sem alterar a estrutura da função.

### 3. Maior Valor da Lista (`Python/desafio3.py`)
* **Conceito:** Algoritmo de busca e comparação em estruturas de repetição (`for`).
* **Destaque:** Construção da lógica de comparação iterativa mantendo um valor de referência (`lista[0]`), sem o uso de funções prontas como `max()`.

### 4. Contagem Regressiva (`Python/desafio4.py`)
* **Conceito:** Laços de repetição com decremento utilizando a função `range()`.
* **Destaque:** Controle de fluxo reverso e intervalo de passos negativos no `for`.

### 5. Sistema de Autenticação com Tentativas (`Python/desafio5.py`)
* **Conceito:** Estrutura condicional `for...else` do Python e Clean Code em validações.
* **Destaque:** Simplificação de retorno booleano direto em expressões de comparação sem `if/else` redundante, combinado com limite de tentativas.

### 6. Filtrar Números Pares de uma Lista (`Python/desafio6.py`)
* **Conceito:** Funções que retornam coleções e o conceito de imutabilidade de dados.
* **Destaque:** Processamento de listas com `.append()` dentro de funções, retornando uma nova lista filtrada sem alterar a original.

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3
* **IDE:** Visual Studio Code
* **Controle de Versão:** Git & GitHub

---

## 🚀 Como Executar

Clone o repositório:
```bash
git clone [https://github.com/nicolasperim/exercicios-python.git](https://github.com/nicolasperim/exercicios-python.git)
