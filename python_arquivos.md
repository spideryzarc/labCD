---
marp: true
theme: default
header: "Revisão de Python - Albert E. F. Muritiba"
# footer: "Laboratório de Ciência de Dados - Albert E. F. Muritiba"
title: "Revisão de Python"
paginate: true
---

# Revisão de Python: Arquivos


---


> Arquivos são usados para armazenar dados em um dispositivo de armazenamento permanente, como um disco rígido.

- Python possui várias funções para criar, ler, atualizar e excluir arquivos diretamente no sistema de arquivos.
- Os podem ser de texto ou binários.
  - Os arquivos de texto podem ser editados com um editor de texto.
  - Os arquivos binários precisam ser manipulados com um programa específico.

---

### Arquivos de Texto

> Arquivos de texto são usados para armazenar dados legíveis por humanos.

- **Criação de Arquivos:** A função `open()` é usada para criar um arquivo.
```python
arquivo = open("arquivo.txt", "w")
arquivo.close()
```
- **Modos de Abertura:** Há vários modos de abertura de arquivos.
  - **`r`:** Leitura (padrão).
  - **`w`:** Escrita.
  - **`a`:** Anexação.
  - **`x`:** Criação. Se o arquivo já existir, a operação falhará.
  
---

- **Escrita em Arquivos:** A função `write()` é usada para escrever em um arquivo.
```python
arquivo = open("arquivo.txt", "w")
arquivo.write("Olá, Mundo!")
arquivo.close()
```
- **Leitura de Arquivos:** A função `read()` é usada para ler um arquivo.
```python
arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
```
---

- **Uso do `with`:** O bloco `with` é usado para garantir que o arquivo seja fechado corretamente.
```python
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```
- **Leitura de Linhas:** A função `readline()` é usada para ler uma linha de cada vez.
```python
with open("arquivo.txt", "r") as arquivo:
    linha = arquivo.readline()
    while linha:
        print(linha)
        linha = arquivo.readline()
```
---

- **Leitura de Linhas:** A função `readlines()` é usada para ler todas as linhas de uma vez.
```python
with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)
```
- **Anexação de Arquivos:** A função `write()` é usada para anexar a um arquivo.
```python
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("\nOlá, Mundo!")
```
---

### Arquivos de Texto Separados por Vírgula (CSV)

> Arquivos CSV são usados para armazenar dados tabulares.
- Cada linha do arquivo é uma linha da tabela.
- Cada valor é separado por vírgula.
- O primeiro linha pode ser um cabeçalho.
  
---

- **Leitura de Arquivos CSV:** A biblioteca `csv` é usada para ler arquivos CSV.
```python
import csv
with open("arquivo.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
```
- **Escrita de Arquivos CSV:** A biblioteca `csv` é usada para escrever arquivos CSV.
```python
import csv
with open("arquivo.csv", "w") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade"])
    escritor.writerow(["Albert", 30])
```
---

### Arquivos de Texto Campos Fixos

> Arquivos de texto com campos fixos são usados para armazenar dados tabulares.
> Cada linha do arquivo é uma linha da tabela.
> Cada campo tem um tamanho fixo.
> O primeiro linha pode ser um cabeçalho.
> A biblioteca `struct` é usada para ler e escrever arquivos com campos fixos.
> A função `pack()` é usada para escrever um registro.
> A função `unpack()` é usada para ler um registro.
>

### Arquivos Binários

