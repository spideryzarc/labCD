---
marp: true
theme: default
header: "Laboratório de Ciência de Dados"
footer: "Albert E. F. Muritiba - (UFC) Curso de Ciência de Dados"
paginate: true
---

# Markdown


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
### Texto

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

### Códigos

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

### Listas

#### Não Ordenadas

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

#### Listas Ordenadas
```markdown
1. Item 1
1. Item 2
1. Item 3
```
1. Item 1
1. Item 2
1. Item 3
---

### Links e Imagens

```markdown
[Texto do Link](https://www.google.com)

![Texto alternativo](caminho/para/imagem.jpg)
```
[Texto do Link](https://www.google.com)

![w:200 ](images/dc3.jpeg)

---

### Tabelas

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

> Alinhar o markdown é opcional, mas é uma boa prática para melhorar a legibilidade.

---
- Alinhamento de colunas: use `:` para alinhar as colunas à esquerda, direita ou centralizado.

```markdown
| Esquerda | Centralizado | Direita |
|:-|:-:|-:|
|  1   |  2   |  3   |
|  4   |  5   |  6   |
```
| Esquerda | Centralizado | Direita |
|:-|:-:|-:|
|  1   |  2   |  3   |
|  4   |  5   |  6   |



---

### Fórmulas

- Markdown suporta fórmulas matemáticas usando LaTeX.

```markdown	
Fórmula em linha $\sum_{i=0}^5 i^2$
Fórmula em bloco:
$$
\int_0^\infty x^2 dx
$$
```

Fórmula em linha $\sum_{i=0}^5 i^2$
Fórmula em bloco:
$$
\int_0^\infty x^2 dx
$$

---

### Blocos de Citação

```markdown
> "Prefiro morrer do que perder a vida."
```
> "Prefiro morrer do que perder a vida."

---

## Conclusão

- Markdown é uma linguagem de marcação leve e fácil de usar.
- É amplamente utilizada para escrever documentação, blogs, e-mails e outros tipos de conteúdo.
- Aprender Markdown é uma habilidade valiosa para qualquer pessoa que trabalha com texto e comunicação.
- Markdown é suportado por muitas plataformas, incluindo GitHub, Jupyter Notebook, Google Colab, entre outros.


---

## Exercícios

1. Crie um arquivo Markdown com um resumo sobre um tema de sua escolha.
2. Adicione títulos, texto formatado, listas, links, imagens e tabelas.


