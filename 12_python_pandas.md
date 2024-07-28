---
marp: true
title: "Curso de Pandas para Ciências de Dados: Conceitos e Elementos Básicos"
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

![bg right:57% ](images/pandas.jpeg)

 # <!--fit--> Pandas
Conceitos e Elementos Básicos


---

![bg right:40% 90%](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png)

# Introdução

#### História e Contexto do Pandas
Pandas, abreviação de "Python Data Analysis Library," foi criado por Wes McKinney em 2008. Foi desenvolvido para fornecer ferramentas de análise e manipulação de dados semelhantes às encontradas em **R** e **Excel**, mas construídas sobre a linguagem de programação **Python**.

[Pandas](https://pandas.pydata.org)

[Python for Data Analysis](https://edisciplinas.usp.br/pluginfile.php/7880239/mod_folder/content/0/Wes%20McKinney%20-%20Python%20for%20Data%20Analysis_%20Data%20Wrangling%20with%20pandas%2C%20NumPy%2C%20and%20Jupyter-OReilly%20Media%20%282022%29.pdf)

---

#### Importância do Pandas na Ciência de Dados

- **Estruturas de Dados Flexíveis**: Essas estruturas permitem a manipulação eficiente e **intuitiva** de dados rotulados, **facilitando operações complexas de dados**.
- **Integração com Outras Bibliotecas**: Pandas é frequentemente usada em conjunto com outras bibliotecas de análise de dados, como NumPy, scipy, Matplotlib, entre outras.
- **Suporte a Diversos Formatos de Dados**: Pandas suporta a leitura e escrita de dados em diversos formatos, como CSV, Excel, SQL, JSON, HTML, entre outros.

---

- **Desempenho e Eficiência**: Se bem utilizada, Pandas pode ser uma ferramenta poderosa para manipulação de dados, haja vista suas operações internas otimizadas e vetorizadas.
- **Comunidade Ativa e Suporte**: Pandas é uma das bibliotecas mais populares para manipulação de dados em Python, com uma comunidade ativa e fóruns de suporte.
  
---

#### Pandas vs SQL

- **Pandas** é uma biblioteca de manipulação de dados em memória, enquanto **SQL** é uma linguagem de consulta a bancos de dados.
- Pandas é mais adequado para operações de **análise exploratória de dados** e **manipulação de dados em memória**, enquanto SQL é mais adequado para **consultas complexas em bancos de dados**.
- Pandas é mais **flexível** e **intuitivo** para operações de análise de dados, enquanto SQL é mais **eficiente** para consultas em bancos de dados.

---

# Estruturas de Dados Fundamentais

### Series

- **Objeto unidimensional** semelhante a um *array*
- **Rótulos de índice** para cada elemento
- dados **homogêneos** (mesmo tipo)

### DataFrames

- **Objeto bidimensional** semelhante a uma **tabela ou planilha**
- **Rótulos de índice** e **colunas** para cada elemento
- **coleção de Series**

> **Nota**: Há outras estruturas de dados no Pandas, mas Series e DataFrames são as mais comuns e amplamente utilizadas.
  
<!-- _footer: "" -->
---

## Criando Series e DataFrames

### Criando Series

```python
import pandas as pd

s = pd.Series([25, 30, 35, 40, 45], 
            index=['Edu', 'Ana', 'Bob', 'Jon', 'Lia'],
            name='Idade')
print(s)
```

> 'pd' é um alias para 'pandas' que é comumente utilizado na comunidade Python.

---

### Criando DataFrames

```python
import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Idade': [25, 30, 35, 40, 45],
    'Salário': [5000, 6000, 7000, 8000, 9000]
}

df = pd.DataFrame(data)

print(df)
```

---

## Módulo 3: Indexação e Seleção de Dados

### Indexação Básica
- Indexação por rótulo e por posição
- Atributos `.loc` e `.iloc`

### Seleção Condicional
- Seleção de dados com condições
- Uso de operadores booleanos

### Alinhamento de Dados
- Alinhamento automático em operações aritméticas
- Uso de métodos `.align()`

---

## Módulo 4: Manipulação de Dados

### Manipulação de Índices
- Redefinição e configuração de índices (`reset_index`, `set_index`)
- Hierarquia de índices (MultiIndex)

### Operações de Agregação e Agrupamento
- Métodos de agregação (`sum`, `mean`, `count`, etc.)
- Agrupamento de dados (`groupby`)

### Operações de Mesclagem e Junção
- Concatenação de DataFrames (`concat`)
- Mesclagem de DataFrames (`merge`, `join`)

---

## Módulo 5: Limpeza e Preparação de Dados

### Tratamento de Dados Faltantes
- Identificação de dados faltantes (`isna`, `notna`)
- Métodos de preenchimento e remoção (`fillna`, `dropna`)

### Transformação de Dados
- Aplicação de funções em dados (`apply`, `map`, `applymap`)
- Manipulação de tipos de dados (`astype`)

### Manipulação de Texto
- Métodos de string (`str`)
- Operações básicas de texto (`replace`, `contains`, `split`)

---

## Módulo 6: Análise Exploratória de Dados (EDA)

### Visualização de Dados
- Introdução ao Matplotlib e Seaborn
- Criação de gráficos básicos com Pandas (`plot`)

### Estatísticas Descritivas
- Métodos de estatísticas descritivas (`mean`, `median`, `mode`, etc.)
- Resumo estatístico com `describe`

---

## Módulo 7: Desempenho e Otimização

### Operações Vetorizadas
- Vantagens das operações vetorizadas
- Aplicação prática em grandes conjuntos de dados

### Uso de DataFrames de Grandes Dimensões
- Leitura e escrita de grandes arquivos (chunking)
- Otimização de desempenho (`dtype`, `memory_usage`)

---

## Módulo 8: Projetos Práticos e Aplicações

### Projeto Integrador
- Aplicação de todos os conceitos aprendidos em um projeto prático
- Análise completa de um conjunto de dados

### Casos de Uso do Mundo Real
- Exemplos de aplicação do Pandas em diferentes indústrias

---

## Recursos Adicionais
- Documentação oficial do Pandas
- Comunidade e fóruns de suporte
- Bibliografia recomendada
