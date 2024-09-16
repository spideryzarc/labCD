---
marp: true
title: "Markdown"
theme: default
class: lead
footer: "Lab. C.D. - Albert E. F. Muritiba"
paginate: true
backgroundColor: #ffffff
# backgroundImage: url('https://marp.app/assets/hero-background.svg')
backgroundImage: url('bg/light_curve2.jpg')
style: |
  .small{
    font-size: 0.75rem;
  }
# Deus é bom o tempo todo
---

# <!-- fit --> Markdown


## Uma linguagem de marcação **leve** e **fácil** de usar.

![bg left:40% fit drop-shadow 80%](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1200px-Markdown-mark.svg.png)

<!-- _backgroundImage: url('bg/light_wall3.jpg') -->

---

## Por que usar Markdown?

Foi criado para ser **simples** de ler e escrever, enquanto ainda permite a formatação de texto de forma **estruturada**.

- **Simplicidade:** Markdown é fácil de aprender e usar.
- **Portabilidade:** Arquivos Markdown podem ser lidos em qualquer editor de texto e podem ser convertidos para HTML, PDF e outros formatos.
- **Versatilidade:** Markdown suporta formatação básica de texto, listas, tabelas, imagens e links.
- **Fórmulas Matemáticas:** Markdown suporta fórmulas matemáticas usando LaTeX.

---

## O que falta no Markdown?

- **Personalização:** Markdown é limitado em termos de personalização e formatação avançada.
- **Bibliografias:** Markdown não suporta referências bibliográficas e citações como LaTeX.
- **Controle de Layout:** Markdown não oferece controle preciso sobre o *layout* do documento. Alinhamento de texto, margens, imagens e outros elementos podem ser difíceis de controlar.

> Alguns desses recursos podem ser adicionados usando extensões e ferramentas de conversão.

---

<!--- _color: '#ffffda' -->

![bg](bg/dark_wood3.jpg)

# ***Markdown*** é uma excelente ferramenta para escrever documentos **simples** e **bem formatados**.

<br>

<p class="small">
Esta apresentação foi escrita em Markdown!
</p>


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

>  O **texto alternativo** é exibido quando a imagem não pode ser carregada.
>  O caminho da imagem pode ser um **URL** ou um **caminho local**.


---

### Alternativas para Imagens

É possível usar HTML para exibir imagens. Desta forma, é possível ter mais controle sobre os atributos da imagem, como largura e altura.

```html
<img src="caminho/para/imagem.jpg" width="800" height="150">
```

<img src="images/dc3.jpeg" width="800" height="150">

---

### Tabelas

```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
| -------- | -------- | -------- |
| Dado 1   | Dado 2   | Dado 3   |
| Dado 4   | Dado 5   | Dado 6   |
```
| Coluna 1 | Coluna 2 | Coluna 3 |
| -------- | -------- | -------- |
| Dado 1   | Dado 2   | Dado 3   |
| Dado 4   | Dado 5   | Dado 6   |

> Alinhar o markdown é opcional, mas é uma boa prática para melhorar a legibilidade.

---
- Alinhamento de colunas: use `:` para alinhar as colunas à esquerda, direita ou centralizado.

```markdown
| Esquerda | Centralizado | Direita |
| :------- | :----------: | ------: |
| 1        |      2       |       3 |
| 4        |      5       |       6 |
```
| Esquerda | Centralizado | Direita |
| :------- | :----------: | ------: |
| 1        |      2       |       3 |
| 4        |      5       |       6 |


---

### Referências cruzadas

```markdown
[Link para o início](#markdown)
```

[Link para o início](#markdown)

> As referências cruzadas são úteis para navegar em documentos longos e complexos.
> Use o título da seção como referência.
> Substitua os espaços por hífens e remova caracteres especiais.


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

# Exercícios

Pesquise sobre um tema do seu interesse e escreva um documento em **Markdown**. Use os recursos aprendidos nesta apresentação. Crie **títulos**, **listas**, **links**, **imagens**, **tabelas** e **fórmulas** matemáticas.



![bg right:30% fit drop-shadow](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1200px-Markdown-mark.svg.png)

<!-- _backgroundImage: url('bg/light_wall2.jpg') -->

