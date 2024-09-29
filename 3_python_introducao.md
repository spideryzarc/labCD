---
marp: true
title: "Revisão de Python"
theme: default
class: lead
footer: "Lab. C.D. - Albert E. F. Muritiba"
paginate: true
backgroundColor: #d6e0e1
# backgroundImage: url('https://marp.app/assets/hero-background.svg')
# backgroundImage: url('bg/light_wall4.jpg')
style: |
  .small{
    font-size: 0.75rem;
  }
  .big{
    font-size: 1.5rem;
  }
# Deus é bom o tempo todo
---

# Não Tão Curta Revisão de Python

Python é uma linguagem de programação de **alto nível, interpretada, orientada a objetos e de tipagem dinâmica**. 

É conhecida por sua **sintaxe simples** e legibilidade.

![bg vertical right:35% 80%](empty.svg)



<!-- _backgroundImage: url('bg/light_desk.jpg') -->

---

## Histórico

- **Guido Van Rossum**, criou o Python. Ele começou em **1989** no Centrum Wiskunde & Informatica (CWI), inicialmente como um projeto de *hobby* para se manter ocupado durante o **Natal**. 
- O nome da linguagem foi inspirado no programa de TV da BBC “**Monty Python’s Flying Circus**”, porque Guido Van Rossum era um grande fã do programa. 

![bg right:40% ](images/silly_walks.jpg)

---

### Principais Marcos

- **1991** - Primeira versão do código Python (versão 0.9.0) foi publicada.
- **1994** - O Python 1.0 foi lançado com novas funções para processar listas, como **mapear**, **filtrar** e **reduzir**.
- **2000** - O Python 2.0 foi lançado com novos recursos úteis, como suporte para caracteres [Unicode](https://pt.wikipedia.org/wiki/Unicode) e um modo mais rápido de percorrer uma lista.
- **2008** - foi lançado o **Python 3.0**. 

[Fonte](https://aws.amazon.com/pt/what-is/python/#:~:text=altera%C3%A7%C3%B5es%20no%20c%C3%B3digo.-,Qual%20%C3%A9%20a%20hist%C3%B3ria%20do%20Python%3F,manter%20ocupado%20durante%20o%20Natal.)

![bg right:15% fit drop-shadow 90%](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png)


---

## Popularidade e Uso

- Python é uma das linguagens de programação **mais populares** do mundo.

![Tiobe Index h:330 drop-shadow](images/tiobe.png)
O índice ***Tiobe*** é uma medida da popularidade de uma linguagem de programação com base na **quantidade de pesquisas** na web.

[Tiobe](https://www.tiobe.com/tiobe-index/)

---

<!--- _color: '#ffffda' -->
<!--- _backgroundImage: url('bg/dark_send.jpg') -->


# <!-- fit --> Quanto **mais popular**,<br> **mais fácil** de encontrar <br> **ajuda** e **recursos**!


---

## Características

### Linguagem Interpretada

- O código é executado linha por linha
- **Vantagem:** 
  - Facilita o desenvolvimento e a depuração,
  - pode ser executado no **modo interativo**,
  - sintaxe mais simples.
- **Desvantagem:** 
  - **Muito mais lento** que linguagens compiladas,
  - o **código-fonte** é distribuído, não o executável
- **Outros exemplos:** JavaScript, Ruby, PHP

---

### Sintaxe Simples

- O Python usa palavras semelhantes às do **inglês**. 
- Esconde a complexidade de tarefas de baixo nível, como **gerenciamento de memória** e arquitetura de computadores.
- **Exemplos:**

em **Python**:
  
```python
a = 5 if i > 0 else 0
# do inglês: "a recebe 5 se i for maior que 0, senão 0"
```
em **C**:
```c
a = i > 0 ? 5 : 0;
// do inglês: "what the hell is this?"
```

---

Olá mundo em **Python**:

```python
print("Olá, Mundo!")
```

Olá mundo em **Java**:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Olá, Mundo!");
    }
}
```

Olá mundo em **C**:

```c
#include <stdio.h>
int main() {
    printf("Olá, Mundo!\n");
    return 0;
}
```

---

### Uma linguagem com tipos dinâmicos

- **Tipagem estática:** O tipo de uma variável é definido em tempo de compilação e não pode ser alterado. Exemplo: C, Java.
- **Tipagem dinâmica:** O tipo de uma variável é definido em tempo de execução e pode ser alterado. Exemplo: Python, JavaScript.

```python
# Em Python, não é necessário definir o tipo da variável antes de usá-la
a = 5
# não há problema em mudar o tipo da variável
a = "cinco"
```

```java
// em Java, é necessário definir o tipo da variável antes de usá-la
int a = 5;
// não é possível mudar o tipo da variável
a = "cinco"; // erro de compilação
```

---

#### Tipagem dinâmica

- **Vantagens:** 
  - **Flexibilidade** para trabalhar com diferentes tipos de dados,
  - **Agilidade** no desenvolvimento,
  - **Menos código** para escrever.
  - **Facilita a prototipação** e a experimentação.
- **Desvantagens:** 
  - **Menos eficiente** que a tipagem estática,
  - **Mais difícil de depurar** e encontrar erros.

> Mesmo o Python 'escondendo' a tipagem, ela ainda existe e é **importante** entender como ela funciona para **evitar erros**.

---

### Orientada a Objetos

- Não abordaremos **POO** neste curso, mas é importante saber que o Python é uma linguagem orientada a objetos. 
- A **grosso modo**, um objeto é uma 'variável' especial que contém **dados** e **métodos** que operam sobre esses dados. Ex.: strings, listas, dicionários, etc.
- [Saiba mais](https://realpython.com/python3-object-oriented-programming/)

---

### Identação

**Identação** é o nome que se dá ao **espaçamento** no início de uma linha de código. 
Em Python, a **identação** é usada para **delimitar blocos de código**.

```python
if x > 0:
    print("x é positivo")
else:
    print("x é negativo")
```

- **Vantagens:** 
  - **Evita a necessidade de chaves** ou palavras-chave para delimitar blocos.
  - **Força a escrita de código mais legível**.
- **Desvantagens:** 
  - **Erros de identação** podem causar problemas.
  - **Ctrl+C, Ctrl+V** pode ser um problema.

---

### <!--fit-->Bibliotecas e Frameworks

<!-- _class: 'invert' -->

# Esta é uma das grandes vantagens de se usar Python. 

## Não só há uma **grande quantidade** de bibliotecas disponíveis, como também são **fáceis de instalar** e usar.

```python
#exemplo instalação de uma biblioteca no Google Colab
!pip install dash
```

![bg blur](bg/dark_flair.jpg)
  
---

## Bibliotecas Python

- **NumPy:** Biblioteca para computação numérica, com suporte para arrays e matrizes multidimensionais.
- **Pandas:** Biblioteca para manipulação e análise de dados, com suporte para estruturas de dados como DataFrames e Series.
- **Scikit-learn:** Biblioteca para aprendizado de máquina, com suporte para algoritmos de classificação, regressão e agrupamento.
- **Matplotlib, Seaborn, Plotly:** Biblioteca para criação de visualizações estáticas, como gráficos de linha, barras e dispersão.
- **TensorFlow, Keras:** Biblioteca para aprendizado de máquina e aprendizado profundo, com suporte para construção e treinamento de modelos de redes neurais.
- **muito mais...**

---

## Frameworks Python

> Um **framework** é uma estrutura de suporte para o desenvolvimento de software. Ele fornece uma base para a criação de aplicativos e oferece uma série de ferramentas e bibliotecas para facilitar o desenvolvimento.

- **Django, Flask, Streamlit:** Framework para desenvolvimento de aplicativos da web, com suporte para criação de sites e APIs.
- **PyTorch:** Framework para aprendizado de máquina e aprendizado profundo, com suporte para construção e treinamento de modelos de redes neurais.
- **Dash:** Framework para criação de aplicativos da web interativos, com suporte para visualizações de dados e painéis de controle.

- **muito mais...**

---

## IDEs Python

***Integrated Development Environment*** é um ambiente que fornece ferramentas para **escrever**, **testar** e **depurar** código.

- Visual Studio Code
- PyCharm
- Spyder
- **Google Colab**
- Jupyter Notebook
- IDLE
- Atom

![bg right:45% fit 98% drop-shadow](images/pycharm.jpeg)
    
---

## Principais Elementos da Linguagem

- **Saída de Dados:** A função `print()` é usada para exibir dados na tela.
- **Entrada de Dados:** A função `input()` é usada para receber dados do usuário.
- **Variáveis:** São usadas para armazenar dados em memória.
- **Operadores:** São usados para realizar operações em variáveis e valores.
- **Estruturas de Controle:** São usadas para controlar o fluxo de execução do programa.
- **Funções:** São usadas para agrupar um conjunto de instruções em um bloco reutilizável.
---

## Outros Elementos da Linguagem

- **Coleções de Dados:** São usadas para armazenar múltiplos valores em uma única variável.
- **Manipulação de Arquivos:** É usado para ler e escrever dados em arquivos.
- **Orientação a Objetos:** É usado para criar e manipular objetos em Python.
- **Tratamento de Exceções:** É usado para lidar com erros e exceções em Python.
- **Módulos e Pacotes:** São usados para organizar e reutilizar código em Python.
- **Bibliotecas e Frameworks:** São usados para estender as funcionalidades do Python.
 
---

## Exercícios de Fixação

1. O que significa que o Python é uma linguagem **interpretada**?
2. Quais as **vantagens** de usar o Python?
3. Quais as **principais bibliotecas** de Python e para que são usadas?
4. Qual a principal **desvantagem** de usar o Python?
5. O que é **identação** e qual a sua importância em Python?

<!-- _backgroundImage: url('bg/light_pencils2.jpg') -->
![bg left:20%](empty.svg)