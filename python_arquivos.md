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



