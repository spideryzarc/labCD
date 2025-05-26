---
marp: true
theme: default
# header: "sqlalchemy - Albert E. F. Muritiba"
# footer: "Laboratório de Ciência de Dados - Albert E. F. Muritiba"
title: "SQLAlchemy"
paginate: true
---

# SQLAlchemy

Uma biblioteca de ORM (Object Relational Mapping) para Python, que fornece uma interface de alto nível para interagir com bancos de dados relacionais.

---

## Instalação

```bash
pip install sqlalchemy
```

---

## Conexão com o Banco de Dados

```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db')
```

Aqui estamos criando uma conexão com um banco de dados SQLite chamado `example.db`. Se o arquivo não existir, ele será criado automaticamente.
A string de conexão pode variar dependendo do banco de dados que você está usando (MySQL, PostgreSQL, etc.). [Outros SGDBs](https://docs.sqlalchemy.org/en/14/dialects/index.html)

---

## Criando uma Tabela

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria o motor de conexão
engine = create_engine("sqlite:///meubanco.db")
# Base para as classes
Base = declarative_base()
# Modelo
class Usuario(Base):
    __tablename__ = 'usuarios' # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True) # Chave primária
    nome = Column(String) # Nome do usuário
    idade = Column(Integer) # Idade do usuário
# Cria as tabelas
Base.metadata.create_all(engine)
```

---

- `Base` é a classe base para todas as classes de modelo, i.e., as classes que representam tabelas no banco de dados devem herdar dela.
- `engine` é o motor de conexão com o banco de dados. 
- `create_all(engine)` cria todas as tabelas definidas nas classes de modelo no banco de dados. Se a tabela já existir, nada acontece.

---

## 🧱 Principais Tipos de Colunas

```python
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime, Text
```

| Tipo         | Descrição                          | Exemplo                    |
|--------------|------------------------------------|----------------------------|
| `Integer`    | Número inteiro                     | `Column(Integer)`          |
| `Float`      | Número com casas decimais          | `Column(Float)`            |
| `String(n)`  | Texto com limite de caracteres     | `Column(String(100))`      |
| `Text`       | Texto longo (sem limite)           | `Column(Text)`             |
| `Boolean`    | Verdadeiro/Falso                   | `Column(Boolean)`          |
| `Date`       | Data (`YYYY-MM-DD`)                | `Column(Date)`             |
| `DateTime`   | Data e hora                        | `Column(DateTime)`         |

---

## ⚙️ Principais Parâmetros

- `primary_key`: Define se o campo é uma chave primária (padrão: `False`).
- `default`: Define um valor padrão para o campo.
- `nullable`: Define se o campo pode ser nulo (padrão: `True`).
- `unique`: Define se o valor do campo deve ser único (padrão: `False`).
- `index`: Cria um índice para o campo (padrão: `False`).
- `autoincrement`: Define se o campo deve ser auto-incrementado (padrão: `False`).

---

### 💡 Exemplo completo

```python
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)
    idade = Column(Integer)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime)
```
- `String(50)`: Define um campo de texto com limite de 50 caracteres.

---
## Recriando do zero

Durante o desenvolvimento, pode ser necessário recriar o banco de dados do zero. Para isso, você pode usar o método `drop_all()` para remover todas as tabelas e depois criar novamente com `create_all()`.
```python
# Remove todas as tabelas
Base.metadata.drop_all(engine)
# Cria novamente as tabelas
Base.metadata.create_all(engine)
```
- **Atenção:** Isso irá apagar todos os dados existentes nas tabelas. Use com cautela, especialmente em ambientes de produção.
- Para evitar a perda de dados, considere usar migrações de banco de dados com ferramentas como [Alembic](https://alembic.sqlalchemy.org/en/latest/).

---

## Inserindo Dados

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine) # Cria uma fábrica de sessões

with Session() as session, session.begin():
    # Cria um novo usuário
    novo_usuario = Usuario(nome='João', idade=30)
    # Adiciona o usuário à sessão
    session.add(novo_usuario)
```
- `sessionmaker` é uma fábrica de sessões que cria novas sessões de banco de dados.
- `session.begin()` inicia uma transação. Se ocorrer um erro, a transação será revertida automaticamente.
- Ao sair do bloco `with`, a sessão é fechada automaticamente e as alterações são salvas no banco de dados.


---


## Consultando Dados

```python
# Consulta todos os usuários
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario.nome, usuario.idade)
```
- `session.query(Usuario)` cria uma consulta para a tabela `usuarios`.
- `all()` retorna todos os resultados da consulta.

---

## Filtrando Dados

```python
# Consulta usuários com idade maior que 25
usuarios_maior_25 = session.query(Usuario).filter(Usuario.idade > 25).all()
for usuario in usuarios_maior_25:
    print(usuario.nome, usuario.idade)
```

---

## Atualizando Dados

```python
# Atualiza a idade de um usuário
usuario = session.query(Usuario).filter(Usuario.nome == 'João').first()
if usuario:
    usuario.idade = 31
    session.commit()
```
- `first()` retorna o primeiro resultado da consulta ou `None` se não houver resultados.
- Após modificar o objeto, `session.commit()` salva as alterações no banco de dados.

---
## Deletando Dados

```python
# Deleta um usuário
usuario = session.query(Usuario).filter(Usuario.nome == 'João').first()
if usuario:
    session.delete(usuario)
    session.commit()
```
- `session.delete(usuario)` marca o objeto para exclusão.
- `session.commit()` salva as alterações no banco de dados.
- Para deletar vários usuários, você pode usar `session.query(Usuario).filter(...).delete()` e depois `session.commit()`.
- Para deletar todos os usuários, use `session.query(Usuario).delete()` e depois `session.commit()`.

---
## Fechando a Sessão

```python
# Fecha a sessão
session.close()
```

- Sempre feche a sessão após terminar de usar para liberar recursos.
- Você pode usar `with` para garantir que a sessão seja fechada automaticamente:
```python
with Session() as session:
    # operações com o banco de dados
    pass
```
- Isso garante que a sessão seja fechada corretamente, mesmo que ocorra um erro durante as operações com o banco de dados.

---

## Chave Estrangeira

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# Modelo de Postagem
class Postagem(Base):
    __tablename__ = 'postagens'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    conteudo = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("Usuario", back_populates="postagens")
# Adiciona a relação na classe Usuario
Usuario.postagens = relationship("Postagem", order_by=Postagem.id, back_populates="usuario")
```
---

- `ForeignKey` define uma chave estrangeira que referencia a tabela `usuarios`.
- `relationship` cria uma relação entre as tabelas, permitindo acessar os dados relacionados de forma mais fácil.
- `back_populates` cria uma relação bidirecional entre as tabelas, permitindo acessar os dados relacionados de ambas as direções.
- `order_by` define a ordem dos resultados quando você consulta os dados relacionados.

---

Para adicionar uma nova postagem para um usuário, você pode fazer o seguinte:

```python
# Cria um novo usuário
novo_usuario = Usuario(nome='Maria', idade=25)
# Cria uma nova postagem
nova_postagem = Postagem(titulo='Meu primeiro post', conteudo='Conteúdo do post', usuario=novo_usuario)
# Adiciona o usuário e a postagem à sessão
session.add(novo_usuario)
session.add(nova_postagem)
# Salva as alterações no banco de dados
session.commit()
```
- Isso cria um novo usuário e uma nova postagem associada a ele.
- O SQLAlchemy cuida de associar a postagem ao usuário automaticamente, graças à relação definida entre as classes.

---

Para consultar as postagens de um usuário, você pode fazer o seguinte:

```python
# Consulta um usuário
usuario = session.query(Usuario).filter(Usuario.nome == 'Maria').first()
if usuario:
    for postagem in usuario.postagens:
        print(postagem.titulo, postagem.conteudo)
```
- Isso consulta o usuário chamado "Maria" e imprime o título e o conteúdo de todas as postagens associadas a ele.

---

Para consultar o usuário de uma postagem, você pode fazer o seguinte:

```python
# Consulta uma postagem
postagem = session.query(Postagem).filter(Postagem.titulo == 'Meu primeiro post').first()
if postagem:
    print(postagem.usuario.nome, postagem.usuario.idade)
```
- Isso consulta a postagem chamada "Meu primeiro post" e imprime o nome e a idade do usuário associado a ela.

---

## Deletando Usuário e Postagens

```python
# Deleta um usuário e suas postagens
usuario = session.query(Usuario).filter(Usuario.nome == 'Maria').first()
if usuario:
    session.delete(usuario)
    session.commit()
```
- Isso deleta o usuário chamado "Maria" e todas as postagens associadas a ele.
- O SQLAlchemy cuida de deletar as postagens associadas automaticamente, graças à relação definida entre as classes.

---

- Para deletar apenas as postagens de um usuário, você pode fazer o seguinte:
```python
# Consulta um usuário
usuario = session.query(Usuario).filter(Usuario.nome == 'Maria').first()
if usuario:
    # Deleta todas as postagens do usuário
    usuario.postagens.clear()
    session.commit()
```
- Isso deleta todas as postagens associadas ao usuário chamado "Maria", mas mantém o usuário no banco de dados.

---

Em alguns casos, usamos uma flag para indicar se o usuário está ativo ou não. Assim, os dados não são deletados, mas apenas marcados como inativos.
```python
# Modelo de Usuário com flag de ativo
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    ativo = Column(Boolean, default=True)  # Flag de ativo
```
- Para marcar um usuário como inativo, você pode fazer o seguinte:
```python
# Consulta um usuário
usuario = session.query(Usuario).filter(Usuario.nome == 'Maria').first()
if usuario:
    usuario.ativo = False
    session.commit()
```
- Isso marca o usuário chamado "Maria" como inativo, mas mantém todos os dados no banco de dados.

---

## Conclusão

SQLAlchemy é uma poderosa biblioteca de ORM para Python que facilita a interação com bancos de dados relacionais. Com ela, você pode criar, consultar, atualizar e deletar dados de forma simples e intuitiva. Além disso, o SQLAlchemy oferece suporte a relacionamentos entre tabelas, permitindo modelar dados complexos de forma eficiente.
- Para mais informações, consulte a [documentação oficial do SQLAlchemy](https://docs.sqlalchemy.org/en/14/).