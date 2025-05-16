---
marp: true
theme: default
# footer: "Laboratório de Ciência de Dados - Albert E. F. Muritiba"
title: "Análise Espacial com Python e OSMnx"
paginate: true
---

# Introdução ao Georreferenciamento

- **Georreferenciamento:** processo de localização espacial.
- Importância dos dados geográficos.
- Aplicações:
  - Planejamento Urbano
  - Logística e Transporte
  - Estudos Ambientais e Econômicos

---

# Conhecendo a OSMnx

- Biblioteca Python especializada em dados geográficos do OpenStreetMap.
- Principais funcionalidades:
  - Geocodificação
  - Análise de redes viárias
  - Visualização de mapas e rotas

Instalação:
```bash
pip install osmnx matplotlib
```

---

# Obtendo Coordenadas de Endereços

**Código:**
```python
def obter_lat_lon(endereco):
    localizacao = ox.geocode(endereco)
    return localizacao
```

- Exemplo:
```python
coord = obter_lat_lon("Avenida Paulista, São Paulo, Brasil")
print(coord)
```

---

# Calculando Distâncias na Malha Viária

**Código:**
```python
def distancia_via(coord_inicio, coord_fim):
    G = ox.graph_from_point(coord_inicio, dist=5000, network_type='drive')
    orig = ox.nearest_nodes(G, coord_inicio[1], coord_inicio[0])
    dest = ox.nearest_nodes(G, coord_fim[1], coord_fim[0])
    distancia = nx.shortest_path_length(G, orig, dest, weight='length')
    return distancia
```

---

# Plotando Mapas Geográficos

**Código:**
```python
def plotar_mapa(localidade):
    G = ox.graph_from_place(localidade, network_type='drive')
    fig, ax = ox.plot_graph(G)
```

- Exemplo prático com localidade conhecida.

---

# Plotando Caminhos Detalhados

**Código:**
```python
def plotar_caminho(coord_inicio, coord_fim):
    G = ox.graph_from_point(coord_inicio, dist=5000, network_type='drive')
    orig = ox.nearest_nodes(G, coord_inicio[1], coord_inicio[0])
    dest = ox.nearest_nodes(G, coord_fim[1], coord_fim[0])
    rota = nx.shortest_path(G, orig, dest, weight='length')
    fig, ax = ox.plot_graph_route(G, rota)
```

- Demonstração visual do trajeto rua a rua.

---

