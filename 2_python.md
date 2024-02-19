---
marp: true
theme: default
header: "Laboratório de Ciência de Dados"
footer: "Albert E. F. Muritiba - (UFC) Curso de Ciência de Dados"
---

# Ambientes Interativos de Análise de Dados

## Um ambiente interativo de análise de dados é uma ferramenta que permite aos usuários explorar, manipular e visualizar dados de forma interativa. 


---
# Exemplos de Ambientes

1. **Jupyter Notebooks**
   - Aplicação web de código aberto para criar documentos que contenham código executável, equações, visualizações e texto explicativo.

2. **RStudio**
   - Ambiente de desenvolvimento integrado (IDE) para a linguagem de programação R, com recursos avançados para análise de dados e geração de relatórios.

---

3. **IBM Watson Studio**
   - Plataforma de ciência de dados e aprendizado de máquina na nuvem, oferecendo ferramentas para explorar, preparar e analisar dados, além de desenvolver modelos de machine learning.
  
4. **Microsoft Azure Notebooks**
   - Serviço baseado em nuvem que permite criar e executar notebooks Jupyter diretamente no navegador, com recursos poderosos de análise de dados e machine learning.

---

5. **Google Colab**
   - Serviço gratuito baseado na nuvem que oferece notebooks Jupyter hospedados no Google Drive, com acesso a recursos de hardware acelerados, como GPUs, para treinamento de modelos de aprendizado profundo.

![bg right:40% fit](images/colab.png)

---

# Google Colab: Uma Visão Geral

- Ambiente de desenvolvimento baseado em nuvem para Python
- Integração com o Google Drive
- Suporte para execução de código em Python
- GPUs e TPUs disponíveis para aceleração de computação

![bg right:40% fit](images/colab.png)

---

# Vantagens do Google Colab

- Acesso gratuito e fácil
- Armazenamento e compartilhamento de notebooks via Google Drive
- Grande variedade de bibliotecas Python disponíveis
- Utilização de hardware acelerado para análises mais rápidas
- Não depende de instalação local de software

---

# Tutorial Google Colab

## Passo 1: Acessando o Google Colab

- Acesse [colab.research.google.com](https://colab.research.google.com/)
- Faça login com sua conta do Google, se necessário

## Passo 2: Criando um Novo Notebook

- Clique em "Novo Notebook" ou acesse "Arquivo" > "Novo Notebook"

## Passo 3: Executando Código

- Células de texto: adicione texto formatado usando Markdown
- Células de código: escreva e execute código Python

---

# Introdução ao Markdown

## O que é Markdown?

- Markdown é uma linguagem de marcação leve com sintaxe fácil de usar.
- Foi criado para ser simples de ler e escrever, enquanto ainda permite a formatação de texto de forma estruturada.

---

## Por que usar Markdown?

- **Simplicidade:** Markdown é fácil de aprender e usar.
- **Portabilidade:** Arquivos Markdown podem ser lidos em qualquer editor de texto e podem ser convertidos para HTML, PDF e outros formatos.
- **Versatilidade:** Markdown suporta formatação básica de texto, listas, tabelas, imagens e links.
- **Fórmulas Matemáticas:** Markdown suporta fórmulas matemáticas usando LaTeX.

---

## Sintaxe Básica

```markdown
# Título 1

## Título 2

### Título 3
```
# Título 1
## Título 2
### Título 3

--- 
## Texto em Markdown

```markdown
**Texto em Negrito**

*Texto em Itálico*

***Texto em Negrito e Itálico***

~~Texto Tachado~~

```
**Texto em Negrito**

*Texto em Itálico*

***Texto em Negrito e Itálico***

~~Texto Tachado~~

---

## Códigos em Markdown

```markdown
`Código em linha`
```
`Código em linha`

```markdown
'''python
for i in range(5):
    print("Olá, Mundo!")
'''
```
```python
for i in range(5):
    print("Olá, Mundo!")
```

---
## Listas em Markdown
### Listas Não Ordenadas
```markdown
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3
```
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3
  
---

### Listas Ordenadas
```markdown
1. Item 1
2. Item 2
3. Item 3
```
1. Item 1
2. Item 2
3. Item 3
---

## Links e Imagens em Markdown

```markdown
[Texto do Link](https://www.google.com)

![w:100](caminho/para/imagem.jpg)
```
[Texto do Link](https://www.google.com)

![w:100 ](images/dc3.jpeg)

---

## Tabelas em Markdown

```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Dado 1   | Dado 2   | Dado 3   |
| Dado 4   | Dado 5   | Dado 6   |
```
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Dado 1   | Dado 2   | Dado 3   |
| Dado 4   | Dado 5   | Dado 6   |

---

## Fórmulas Matemáticas em Markdown

```markdown
$$
\int_0^\infty x^2 dx
$$
```
$$
\int_0^\infty x^2 dx
$$

---


# Revisão de Python

## Histórico

- Guido Van Rossum, criou o Python. Ele começou em 1989 no Centrum Wiskunde & Informatica (CWI), inicialmente como um projeto de hobby para se manter ocupado durante o Natal. 
- O nome da linguagem foi inspirado no programa de TV da BBC “Monty Python’s Flying Circus”, porque Guido Van Rossum era um grande fã do programa. 



---

## Principais Marcos

Guido Van Rossum publicou a primeira versão do código Python (versão 0.9.0) em 1991. Ela já incluía bons recursos, como alguns tipos de dados e funções para tratamento de erros. 
O Python 1.0 foi lançado em 1994 com novas funções para processar facilmente uma lista de dados, como mapear, filtrar e reduzir.
O Python 2.0 foi lançado em 16 de outubro de 2000, com novos recursos úteis para programadores, como suporte para caracteres Unicode e um modo mais rápido de percorrer uma lista.
Em 3 de dezembro de 2008, foi lançado o Python 3.0. Ele incluía recursos como a função de impressão e mais suporte para divisão de números e tratamento de erros. 

[fonte](https://aws.amazon.com/pt/what-is/python/#:~:text=altera%C3%A7%C3%B5es%20no%20c%C3%B3digo.-,Qual%20%C3%A9%20a%20hist%C3%B3ria%20do%20Python%3F,manter%20ocupado%20durante%20o%20Natal.)

---

## Popularidade e Uso

- Python é uma das linguagens de programação mais populares do mundo, conhecida por sua sintaxe simples e legibilidade.
- É amplamente utilizado em uma variedade de campos, incluindo ciência de dados, desenvolvimento web, automação de sistemas, inteligência artificial e muito mais.




## Passo 4: Importando Dados

- Monte o Google Drive para acessar seus arquivos
- Use bibliotecas Python como Pandas para importar conjuntos de dados

---

## Passo 5: Visualizando e Analisando Dados

- Utilize bibliotecas como Matplotlib e Seaborn para criar visualizações
- Realize análises exploratórias de dados para extrair insights

---

## Passo 6: Salvando e Compartilhando seu Notebook

- Salve seu trabalho no Google Drive
- Compartilhe o link do seu notebook com outras pessoas

---

# Conclusão

- O Google Colab é uma ferramenta poderosa para análise de dados baseada em nuvem, oferecendo acesso gratuito e fácil, suporte para execução de código Python e integração com o Google Drive. Com este tutorial básico, você está pronto para começar a explorar e trabalhar com dados no Google Colab!
