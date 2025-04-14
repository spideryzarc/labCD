import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import folium

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

# Plotar um mapa interativo dado um polígono ou localidade
def plotar_mapa_interativo(localidade):
    G = ox.graph_from_place(localidade, network_type='drive')
    nodes, edges = ox.graph_to_gdfs(G)
    centro = nodes.geometry.iloc[0].y, nodes.geometry.iloc[0].x
    mapa = folium.Map(location=centro, zoom_start=13)
    for _, edge in edges.iterrows():
        pontos = [(p[0], p[1]) for p in edge.geometry.coords]
        folium.PolyLine(pontos, color="blue", weight=2.5).add_to(mapa)
    mapa.save("mapa_interativo.html")
    print("Mapa interativo salvo como 'mapa_interativo.html'.")

# Plotar o caminho entre duas coordenadas (rua a rua)
def plotar_caminho(coordenada_inicio, coordenada_fim):
    G = ox.graph_from_point(coordenada_inicio, dist=5000, network_type='drive')
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    rota = nx.shortest_path(G, orig, dest, weight='length')
    fig, ax = ox.plot_graph_route(G, rota)

# Plotar o caminho interativo entre duas coordenadas (rua a rua)
def plotar_caminho_interativo(coordenada_inicio, coordenada_fim):
    G = ox.graph_from_point(coordenada_inicio, dist=5000, network_type='drive')
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    rota = nx.shortest_path(G, orig, dest, weight='length')
    nodes, edges = ox.graph_to_gdfs(G)
    centro = nodes.geometry.iloc[0].y, nodes.geometry.iloc[0].x
    mapa = folium.Map(location=centro, zoom_start=13)
    rota_coords = [(nodes.loc[node].geometry.y, nodes.loc[node].geometry.x) for node in rota]
    folium.PolyLine(rota_coords, color="red", weight=2.5).add_to(mapa)
    mapa.save("caminho_interativo.html")
    print("Caminho interativo salvo como 'caminho_interativo.html'.")

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
    plotar_mapa_interativo(localidade)

    plotar_caminho(coord1, coord2)
    plotar_caminho_interativo(coord1, coord2)