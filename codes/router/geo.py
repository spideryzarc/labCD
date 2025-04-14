import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Configuração inicial do OSMnx
ox.settings.use_cache = True
ox.settings.log_console = True

# Retorna latitude e longitude dado um endereço
def obter_lat_lon(endereco):
    localizacao = ox.geocode(endereco)
    return localizacao

# Retorna distância na malha viária dado duas coordenadas
def distancia_via(coordenada_inicio, coordenada_fim):
    G = ox.graph_from_point(coordenada_inicio, dist=5000, network_type='drive')
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    distancia = nx.shortest_path_length(G, orig, dest, weight='length')
    return distancia

# Plotar um mapa dado um polígono ou localidade
def plotar_mapa(localidade):
    G = ox.graph_from_place(localidade, network_type='drive')
    fig, ax = ox.plot_graph(G)

# Plotar o caminho entre duas coordenadas (rua a rua)
def plotar_caminho(coordenada_inicio, coordenada_fim):
    G = ox.graph_from_point(coordenada_inicio, dist=5000, network_type='drive')
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    rota = nx.shortest_path(G, orig, dest, weight='length')
    fig, ax = ox.plot_graph_route(G, rota)

# Exemplo de uso
if __name__ == "__main__":
    endereco = "Avenida Paulista, São Paulo, Brasil"
    coord1 = obter_lat_lon(endereco)
    print(f"Coordenadas do endereço '{endereco}': {coord1}")

    coord2 = (-23.550520, -46.633308) # Centro de São Paulo

    distancia = distancia_via(coord1, coord2)
    print(f"Distância viária entre os pontos: {distancia:.2f} metros")

    localidade = "Centro, Fortaleza, Ceará, Brasil"
    plotar_mapa(localidade)

    plotar_caminho(coord1, coord2)