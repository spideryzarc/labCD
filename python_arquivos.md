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
### Arquivos de Texto com Dados Estruturados

- Esses arquivos possuem uma estrutura arbitrária, mas bem definida.
- Eles são usados para armazenar dados que podem ser usados para testar algoritmos e programas.
- Exemplos:
  - O site [The Matrix Market](https://math.nist.gov/MatrixMarket/) é um repositório de dados de matrizes esparsas.

  - O site [The DIMACS Graph Format](http://www.diag.uniroma1.it/challenge9/format.shtml) é um repositório de dados de problemas de otimização.

  - O site [TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) é um repositório de dados de problemas de otimização.

---

- Para ler esses dados, é necessário entender a estrutura do arquivo que está, geralmente, descrita no site onde os dados estão disponíveis.
- Para algumas fontes muito populares, como o TSPLIB, existem bibliotecas que podem ser usadas para ler os dados.

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

### Arquivos de Texto Campos de largura fixa

- Arquivos de texto com campos fixos são usados para armazenar dados tabulares.
- Cada linha do arquivo é uma linha da tabela.
- Cada campo tem um tamanho fixo.


---

- É possível usar slicing para ler arquivos com campos de largura fixa.
- A função `strip()` é usada para remover espaços em branco.
```python
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        nome = linha[0:10].strip()
        idade = linha[10:12].strip()
        print(nome, idade)
```

---

- Para escrever arquivos com campos de largura fixa, é possível usar a função `format()`.
```python
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("{:10}{:2}\n".format("Albert", 30))
```

---
### Arquivos texto JSON

- Arquivos JSON são usados para armazenar dados estruturados.
- A biblioteca `json` é usada para ler e escrever arquivos JSON.
- A função `dump()` é usada para escrever um arquivo JSON.
```python
import json
dados = {"nome": "Albert", "idade": 30}
with open("arquivo.json", "w") as arquivo:
    json.dump(dados, arquivo)
```
- A função `load()` é usada para ler um arquivo JSON.
```python
import json
with open("arquivo.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)
```
---
> Um outro formato de arquivo estruturado é o XML. Ao contrário do JSON, este formato é complexo e não é nativo do Python. Não abordaremos este formato aqui.

 [Ver mais](https://aws.amazon.com/pt/compare/the-difference-between-json-xml/#:~:text=Additionally%2C%20both%20formats%20are%20self,XML%20are%20still%20commonly%20used.) 


---
### Arquivos Binários
> Arquivos binários são usados para armazenar dados não legíveis por humanos.

- Vantagens:
  - Compactação.
  - Velocidade.
  - Segurança.
- Desvantagens:
  - Não legíveis por humanos.
  - Difíceis de editar.

---

- Escrevendo uma lista de números inteiros em um arquivo binário.
```python
numeros = [1, 2, 3, 4, 5]
with open("arquivo.bin", "wb") as arquivo:
    for numero in numeros:
        arquivo.write(numero.to_bytes(4, "little"))
```
- Lendo uma lista de números inteiros de um arquivo binário.
```python
numeros = []
with open("arquivo.bin", "rb") as arquivo:
    while True:
        numero = arquivo.read(4)
        if not numero:
            break
        numeros.append(int.from_bytes(numero, "little"))
print(numeros)

```
--- 

- Escrevendo um texto em um arquivo binário.
```python
texto = "Olá, Mundo!"
with open("arquivo.bin", "wb") as arquivo:
    arquivo.write(texto.encode("utf-8"))
```
- Lendo um texto de um arquivo binário.
```python
with open("arquivo.bin", "rb") as arquivo:
    texto = arquivo.read().decode("utf-8")
    print(texto)
```

> A função `encode()` é usada para converter uma string em bytes.
> A função `decode()` é usada para converter bytes em uma string.
---

- A biblioteca `pickle` é usada para ler e escrever arquivos binários.
- A função `dump()` é usada para escrever um arquivo binário.
```python
import pickle
dados = {"nome": "Albert", "idade": 30}
with open("arquivo.bin", "wb") as arquivo:
    pickle.dump(dados, arquivo)
```
- A função `load()` é usada para ler um arquivo binário.
```python
import pickle
with open("arquivo.bin", "rb") as arquivo:
    dados = pickle.load(arquivo)
    print(dados)
```
---

## Exercícios






