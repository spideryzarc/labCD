---
marp: true
title: "Laboratório de Ciência de Dados - Apresentação"
theme: default
class: lead
footer: "Lab. C.D. - Albert E. F. Muritiba"
paginate: true
backgroundColor: #ffffff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
style: |
  .small{
    font-size: 0.75rem;
  }
# Deus é bom o tempo todo
---


# <!--fit--> Introdução

<br>

## Laboratório de Ciência de Dados 

![bg right:65%](images/dc5.jpeg)

---

# Objetivos:

- Capacitar os alunos com habilidades **práticas** essenciais para trabalhar com dados de forma **eficiente**.
- Preparar os alunos para enfrentar **desafios reais** em análise de dados e tomar decisões fundamentadas com base em evidências.
- Explorar as **bibliotecas e ferramentas** mais populares para análise de dados em Python.


---

# Bibliografia

<!-- _backgroundImage: url('bg/light_book.jpg') -->

![bg right:20% fit 90% drop-shadow ](images/PDSH-cover.png)
  - MENEZES, Nilo Ney Coutinho. **Introdução à programação com Python: algoritmos e lógica de programação para iniciantes**.
  
  - VANDERPLAS, Jake. **Python Data Science Handbook**. [on-line](https://jakevdp.github.io/PythonDataScienceHandbook/).
   
  - HETLAND, Magnus Lie; SPRINGERLINK (ONLINE SERVICE). **Python Algorithms: Mastering Basic Algorithms in the Python Language**. 
  
  - BERTHOLD, M. et al. **Guide to Intelligent Data Analysis : How to Intelligently Make Sense of Real Data**  [on-line](http://dx.doi.org/10.1007/978-1-84882-260-3).

---

# O que é Ciência de Dados?

- O termo "cientista de dados" foi cunhado por **D.J. Patil**. Ele foi o Cientista Chefe do *LinkedIn*. Em 2011

- Um cientista de dados **faz perguntas** únicas e interessantes sobre os dados para gerar *insights* rigorosos e úteis.


- O papel dos cientistas de dados é gerar **inteligência** de negócios **aplicável**, transformando organizações e sociedades.


![bg left:30%](images/dc6.jpeg)

---
<!-- _backgroundImage: url('bg/yellow_pencil.jpg') -->
<!-- _color: white -->

![bg left:25%](bg/empty.svg)

 # "Um cientista de dados é alguém que é melhor em **estatística** do que qualquer programador e melhor em **programação** do que qualquer estatístico."

---

# Áreas do conhecimento

- **Matemática** e **Estatística**
- **Computação** (programação, banco de dados, etc.)
- **Comunicação** (escrita, visualização de dados, etc.)
- **Áreas específicas** de aplicação (saúde, finanças, marketing, etc.)

![bg right:40%](images/dc1.jpeg)

---

# Importância da Ciência de Dados

- Geração de *insights* valiosos a partir de dados
- Auxílio na **tomada de decisões** estratégicas
- Impacto em diversas áreas da sociedade

![bg left](images/dc4.jpeg)

---

# Exemplos de Aplicações

- **Saúde**: Análise de dados clínicos para diagnóstico e tratamento
- **Finanças**: Previsão de mercado e análise de risco
- **Marketing**: Segmentação de mercado e personalização de campanhas
- **Transporte**: Otimização de rotas e logística

---

## Prevenção de Tsunami

- **Stanford University** criou um sistema de alerta precoce de tsunamis que usa aprendizado de máquina.
- Auxilia geocientistas na preparação e mitigação dos impactos de desastres naturais.
- [Fonte](https://www.springboard.com/blog/data-science/data-science-case-studies/)

![bg right:30% fit 150% drop-shadow](https://1000logos.net/wp-content/uploads/2018/02/Stanford-University-Logo-500x281.png)

---

## Saúde: Deteção de Câncer Metastático

- O **LYNA** do Google utiliza IA para detectar câncer metastático em linfonodos.
- Acurácia de 99% em diagnósticos de câncer.
- [Fonte](https://www.springboard.com/blog/data-science/data-science-case-studies/)

![bg right:40% fit 95% drop-shadow](https://indianexpress.com/wp-content/uploads/2018/10/google_lymph_1.jpg)

---

## Logística: UPS

- O ***Network Planning Tools*** (NPT) da UPS usa aprendizado de máquina para otimizar rotas de entrega.
- Economiza combustível e aumenta a eficiência logística.
- [Fonte](https://www.springboard.com/blog/data-science/data-science-case-studies/)

![bg right:40% fit 95% drop-shadow](https://logos-world.net/wp-content/uploads/2020/01/UPS-Logo-2014-present-700x394.png)

---

## E-commerce: Amazon

- **Amazon** usa um motor de recomendação baseado em aprendizado de máquina.
- Gera 35% de sua receita anual ao recomendar produtos personalizados.
- [Fonte](https://www.springboard.com/blog/data-science/data-science-case-studies/)

![bg right:40% fit 80% drop-shadow](https://logodownload.org/wp-content/uploads/2014/04/amazon-logo.png)

---

# O que são *insights*?

- **Compreensão repentina de um problema**, ocasionada por uma percepção mental clara e, geralmente intuitiva, dos elementos que levam a sua resolução.
- **Iluminação**; revelação ou visão inesperada e repentina de alguma coisa.
- [Psiquiatria] Autoconhecimento; habilidade de julgar com objetividade a sua própria maneira de agir.
- [Religião] Expressão de um conhecimento místico; visão mística.

[Fonte](https://www.dicio.com.br/insight/)


---

Alternativas em português para *insight*:
- **Percepção**
- **Intuição**
- **Entendimento**
- **Revelação**
- **Visão**
- **Iluminação**
- **Estalo**
- **Sacada**

![bg left:40% fit 90% drop-shadow](https://s1.static.brasilescola.uol.com.br/be/conteudo/images/2-bandeira-do-brasil.jpg)

---

# Conteúdo Programático

1. **Ambiente de Desenvolvimento Iterativo** (Jupyter Notebook / Google Colab)
2. **Markdown** 
3. **Python Básico** -- Revisão e aprofundamento de conceitos básicos:
   1. **Sinatxe Básica** - Variáveis, operadores, estruturas de controle, E/S ...
   2. **Estruturas de Dados** - Listas, tuplas, dicionários e conjuntos.
   3. **Funções** - Definição, argumentos, retorno, escopo, lambda, geradores ...
   4. **Strings** - Métodos, formatação...
   5. **Arquivos** - Leitura e escrita de arquivos de texto e binários.

---

4. **Estatística Descritiva** - Conceitos básicos de estatística descritiva em Python.
5. **Visualização de Dados** - Bibliotecas para visualização de dados em Python.
6. **Análise de Dados** - Manipulação e análise de dados com **Pandas**. Estruturas de dados, leitura e escrita de dados, indexação, seleção, filtragem, agrupamento, junção, etc.
7. **Projeto de Análise de Dados** - Projeto prático de análise de dados com **Pandas**.
  

---

# Conclusão

A **ciência de dados** desempenha um papel central na **transformação** de **dados** brutos em percepções acionáveis, influenciando **decisões** estratégicas em setores críticos, como saúde, finanças e transporte.

---

# Exercícios

- O que é um cientista de dados?
- Quais são as áreas do conhecimento que compõem a ciência de dados?
- Quais são as aplicações da ciência de dados em diferentes áreas?
- Qual é a importância da ciência de dados para a sociedade?
- Quais são os exemplos de aplicações da ciência de dados em diferentes áreas?
