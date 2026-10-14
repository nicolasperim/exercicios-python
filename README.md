# 🐍 Exercícios de Lógica e Fundamentos em Python

Repositório criado para registrar minha evolução nos fundamentos de programação e lógica com Python, aplicando boas práticas de código (**Clean Code**), modularização com funções e manipulação de estruturas de dados.

---

## 📌 Desafios Concluídos

### 🟢 Módulo 1: Fundamentos, Controle de Fluxo e Funções

1. **Verificador de Paridade** (`Python/desafio01.py`)
   - **Conceito:** Separação da regra de negócio (função) da interface do usuário.
   - **Destaque:** Uso de retornos booleanos (`True` / `False`) em vez de mensagens diretas, tornando a função reutilizável.

2. **Calculadora de Média Escolar** (`Python/desafio02.py`)
   - **Conceito:** Passagem de listas como parâmetros em funções.
   - **Destaque:** Implementação dinâmica utilizando `sum()` e `len()`, permitindo calcular médias para qualquer quantidade de notas sem alterar a estrutura da função.

3. **Maior Valor da Lista** (`Python/desafio03.py`)
   - **Conceito:** Algoritmo de busca e comparação em estruturas de repetição (`for`).
   - **Destaque:** Construção da lógica de comparação iterativa mantendo um valor de referência (`lista[0]`), sem o uso de funções prontas como `max()`.

4. **Contagem Regressiva** (`Python/desafio04.py`)
   - **Conceito:** Laços de repetição com decremento utilizando a função `range()`.
   - **Destaque:** Controle de fluxo reverso e intervalo de passos negativos no `for`.

5. **Soma de Números Pares num Intervalo** (`Python/desafio05.py`)
   - **Conceito:** Acumulação de valores e verificação de condições com operador resto (`%`).
   - **Destaque:** Filtragem e soma acumulativa dentro de laços de repetição.

6. **Gerador de Tabuada** (`Python/desafio06.py`)
   - **Conceito:** Interatividade com o usuário e laços para geração de sequências matemáticas.
   - **Destaque:** Formatação limpa de saídas estruturadas.

7. **Inversor de String Manual** (`Python/desafio07.py`)
   - **Conceito:** Manipulação iterativa de sequências e strings.
   - **Destaque:** Reversão realizada manualmente via laço `for`, evitando *slicing* direto (`[::-1]`) para consolidar o entendimento algorítmico.

8. **Contador de Vogais** (`Python/desafio08.py`)
   - **Conceito:** Busca de subelementos em strings e conversão para caixa baixa (`.lower()`).
   - **Destaque:** Trata diferenças entre maiúsculas/minúsculas e itera diretamente sobre os caracteres.

9. **Fatorial de um Número** (`Python/desafio09.py`)
   - **Conceito:** Estrutura de repetição para produto acumulado.
   - **Destaque:** Tratamento de casos especiais como $0! = 1$ e $1! = 1$.

10. **Busca do Segundo Maior Valor** (`Python/desafio10.py`)
    - **Conceito:** Algoritmo de ordenação/varredura sem o uso de `sort()` ou `max()`.
    - **Destaque:** Raciocínio lógico para rastrear simultaneamente o maior e o segundo maior elemento em uma única passagem.

---

### 🟡 Módulo 2: Estruturas de Dados Intermediárias (Dicionários)

11. **Registro e Validação de Boletim de Aluno** (`Python/desafio11.py`)
    - **Conceito:** Manipulação de Dicionários e validação de dados com laço `while`.
    - **Destaque:** Mapeamento de chave-valor (`nome`, `nota`), validação estrita do intervalo da nota (`0.0` a `10.0`) com operador lógico `or` e modularização da verificação de aprovação.

---

## 🛠️ Tecnologias e Boas Práticas
- **Linguagem:** Python 3
- **Padrão de Código:** PEP 8
- **Estilo de Documentação:** Google Style Docstrings
- **Controle de Versão:** Git & GitHub
