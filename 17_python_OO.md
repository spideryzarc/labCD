---
marp: true
title: "Orientação a Objetos - Python"
theme: default
class: lead
footer: "Laboratório de Ciência de Dados- Estatística - Albert E. F. Muritiba"
paginate: true
backgroundColor: #ffffff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
style: |
  .small{
    font-size: 0.75rem;
  }
---

# Orientação a Objetos - Python

Um programa pode ser visto como um conjunto de objetos que interagem entre si.

![bg right](empty.png)

---
# Paradigmas de Programação

Dentre os paradigmas de programação, podemos destacar:
- **Programação Estruturada**: Baseia-se em estruturas de controle (if, for, while) e funções. O foco é na sequência de instruções a serem executadas.
- **Programação Funcional**: Enfatiza o uso de funções puras e evita efeitos colaterais. O foco é na transformação de dados através de funções.
- **Programação Orientada a Objetos (POO)**: Organiza o código em objetos que encapsulam dados e comportamentos. O foco é na interação entre objetos.

> Elas não são mutuamente excludentes. O programador pode usar mais de um paradigma em um mesmo programa.

---

# Objetos
Um objeto é uma instância de uma classe. Ele possui:
- **Atributos**: Características ou propriedades do objeto.
- **Métodos**: Funções que definem o comportamento do objeto.
- **Estado**: Conjunto de valores dos atributos em um dado momento.


> De forma geral, um objeto é uma estrutura de dados que combina dados e funções que operam sobre esses dados.
---
# Classes

Uma classe é um modelo ou molde para criar objetos. 

- O que o programador "escreve" é a classe.
- Os objetos são "variáveis" geradas a partir da classe.
- Tecnicamente, uma classe é um **tipo de dado** definido pelo programador e os objetos são **instâncias** desse tipo de dado.

---
# Definindo uma Classe

```python
class Retangulo:
  # Atributos
  base = 0
  altura = 0
  # Métodos
  def area(self):
    return self.base * self.altura
  def perimetro(self):
    return 2 * (self.base + self.altura)
```
> A palavra-chave `class` é usada para definir uma classe. O nome da classe deve começar com letra maiúscula por convenção.
---
# Métodos

Os métodos são funções definidas dentro da classe. Eles têm acesso aos atributos do objeto através do parâmetro `self`, que representa a instância atual da classe.

O código abaixo está errado em Python!
```python
class Retangulo:
  # Atributos
  base = 0
  altura = 0
  # Métodos
  def area():
    return base * altura # Erro!
``` 

---

Comumente, quando estamos programando uma classe, pensamos como se uma **outra pessoa** fosse usar a classe. Tentamos "esconder" o máximo possível os detalhes de implementação, e deixar o uso da classe o mais simples possível.

- O programador que vai usar a classe não precisa saber como a classe foi implementada.
- Assim como você não faz ideia de como um dicionário é implementado, mas sabe como usá-lo.

---

# Criando Objetos
```python
# Criando um objeto da classe Retangulo
r1 = Retangulo()
# Acessando os atributos
r1.base = 5
r1.altura = 10
# Chamando os métodos
area = r1.area()
perimetro = r1.perimetro()
print(f"Área: {area}, Perímetro: {perimetro}")
```
> O objeto `r1` é uma instância da classe `Retangulo`. Os atributos `base` e `altura` são acessados diretamente, e os métodos são chamados usando a **notação de ponto**.

---
# Breve Comentário

- A principal vantagem da POO é a **abstração**. O programador pode pensar em termos de objetos e suas interações, em vez de se preocupar com detalhes de implementação.
- Por exemplo, o programador pode "esquecer" ou "ignorar" que `r1` se resume a um conjunto de variáveis e funções. O programador pode pensar que `r1` é um retângulo, e que vai se comportar como um retângulo.

> Outra vantagens são mais complexas, como **herança**, **polimorfismo** e **encapsulamento**. Vamos ver cada uma delas mais adiante.
---

# Métodos Especiais
Os métodos especiais são funções que permitem definir o comportamento de um objeto em situações específicas. Eles começam e terminam com dois underscores (`__`).
Vamos ver alguns exemplos:
- `__init__(self, ...)`: Construtor da classe. É chamado quando um objeto é criado.
- `__repr__(self)`: Método chamado quando o objeto é representado como string (ex: `str(objeto)`).

---
# Construtor

```python
class Retangulo:
  # Construtor
  def __init__(self, base, altura):
    if base <= 0 or altura <= 0:
      raise ValueError("Base e altura devem ser maiores que zero.")
    self.base = base
    self.altura = altura
  # Métodos
  def __repr__(self):
    return f"Ret(base={self.base}, altura={self.altura})"
  def area(self):
    return self.base * self.altura
  def perimetro(self):
    return 2 * (self.base + self.altura)
```
---
# Criando Objetos com Construtor

```python
# Criando um objeto da classe Retangulo
r1 = Retangulo(5, 10)
# Imprimindo o objeto
print(r1)
>> Ret(base=5, altura=10)
```
Ficou mais prático, não é mesmo?
- O construtor `__init__` é chamado automaticamente quando o objeto é criado. 
- O método `__repr__` é chamado quando o objeto é convertido para string, permitindo uma representação mais legível.
---
# Outro Breve Comentário

Mesmo que você não soubesse, você já usou objetos no Python.
- Listas, dicionários, strings, etc. são todos objetos.
- Eles têm métodos especiais e podem ser manipulados como objetos.
- Por exemplo, a lista `[1, 2, 3]` é um objeto da classe `list`, e tem métodos como `append()`, `remove()`, etc.
- O dicionário `{"a": 1, "b": 2}` é um objeto da classe `dict`, e tem métodos como `keys()`, `values()`, etc.

---

Mesmo evitando números negativos na construção do objeto, ainda podemos atribuir, erroneamente, valores negativos aos atributos `base` e `altura` depois que o objeto foi criado.

```python
r1 = Retangulo(5, 10)
r1.base = -5
print(r1.area()) # -50
```

Seria interessante evitar isso, não é mesmo?

---
# Emcapsulamento

Um dos pontos fracos do Python é que ele não tem um sistema fácil de controle de acesso.
- Não existe o conceito de `private`, `protected` e `public` como em outras linguagens.
- O Python tem uma convenção de nomenclatura para **sugere** que um atributo ou método é "privado" (ou seja, não deve ser acessado diretamente fora da classe).
- Isso é feito prefixando o nome do atributo ou método com um underscore (`_`).
---
## Exemplo de Encapsulamento

Se queremos **sugerir** que `base` e `altura` não devem ser acessados diretamente, podemos fazer o seguinte:
```python
class Retangulo:
  def __init__(self, base, altura):
    if base <= 0 or altura <= 0:
      raise ValueError("Base e altura devem ser maiores que zero.")
    self._base = base
    self._altura = altura
  def area(self):
    return self._base * self._altura
  def perimetro(self):
    return 2 * (self._base + self._altura)
```
> Isso não impede o acesso direto.

---

Em Python, o "usuário" de uma classe teria acesso ao código fonte da classe, daì proibir o acesso direto não faria sentido.

Em outras linguagens, como Java, o encapsulamento é mais rigoroso.

```python
r1 = Retangulo(5, 10)
r1._base = -5 # Acesso direto ao atributo
print(r1.area()) # -50
```
> O programador pode acessar o atributo `_base` diretamente, mas sabe que pode "estragar" o objeto.
> Há formas de dificultar o acesso direto, mas não é o foco aqui.
---

# Mais Métodos Especiais

- `__eq__(self, other)`: Permite que você defina a própria lógica de comparação entre objetos. Por exemplo, se dois retângulos têm a mesma base e altura, eles são considerados iguais.
```python
class Retangulo:
  # ...
  def __eq__(self, other):
    if not isinstance(other, Retangulo):
      return False
    return self._base == other._base and self._altura == other._altura
```
```python
r1 = Retangulo(5, 10)
r2 = Retangulo(5, 10)
print(r1 == r2) # True
```

> Quando `__eq__` não está definido, o Python compara os objetos por identidade (ou seja, se são o mesmo objeto na memória).