import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import folium
import os
import pickle

# Configuração inicial do OSMnx para usar cache e exibir logs no console
ox.settings.use_cache = True
ox.settings.log_console = True

# Caminho para salvar o grafo localmente
GRAFO_PATH = "grafo_centro_fortaleza.pkl"

# Função para carregar ou baixar o grafo do Centro de Fortaleza
def carregar_grafo():
    if os.path.exists(GRAFO_PATH):
        # Carrega o grafo salvo localmente
        with open(GRAFO_PATH, "rb") as f:
            G = pickle.load(f)
        print("Grafo carregado do arquivo local.")
    else:
        # Baixa o grafo do Centro de Fortaleza e salva localmente
        print("Baixando o grafo do Centro de Fortaleza...")
        G = ox.graph_from_place("Centro, Fortaleza, Ceará, Brasil", network_type='drive')
        with open(GRAFO_PATH, "wb") as f:
            pickle.dump(G, f)
        print("Grafo salvo localmente.")
    return G

# Função para obter latitude e longitude a partir de um endereço
def obter_lat_lon(endereco):
    # Geocodifica o endereço para obter as coordenadas
    localizacao = ox.geocode(endereco)
    return localizacao

# Função para calcular a distância viária entre duas coordenadas
def distancia_via(coordenada_inicio, coordenada_fim, G):
    # Encontra os nós mais próximos das coordenadas inicial e final
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    # Calcula a distância mais curta entre os nós no grafo
    distancia = nx.shortest_path_length(G, orig, dest, weight='length')
    return distancia

# Função para plotar um mapa estático de uma localidade
def plotar_mapa(localidade):
    # Cria um grafo viário para a localidade especificada
    G = ox.graph_from_place(localidade, network_type='drive')
    # Plota o grafo em um mapa estático
    fig, ax = ox.plot_graph(G)

# Função para plotar um mapa interativo de uma localidade
def plotar_mapa_interativo(localidade):
    # Cria um grafo viário para a localidade especificada
    G = ox.graph_from_place(localidade, network_type='drive')
    # Converte o grafo em DataFrames de nós e arestas
    nodes, edges = ox.graph_to_gdfs(G)
    # Define o centro do mapa como a localização do primeiro nó
    centro = nodes.geometry.iloc[0].y, nodes.geometry.iloc[0].x
    # Cria um mapa interativo com Folium
    mapa = folium.Map(location=centro, zoom_start=13)
    # Adiciona as arestas do grafo ao mapa como linhas
    for _, edge in edges.iterrows():
        pontos = [(p[0], p[1]) for p in edge.geometry.coords]
        folium.PolyLine(pontos, color="blue", weight=2.5).add_to(mapa)
    # Salva o mapa interativo em um arquivo HTML
    mapa.save("mapa_interativo.html")
    print("Mapa interativo salvo como 'mapa_interativo.html'.")

# Função para plotar o caminho estático entre duas coordenadas
def plotar_caminho(coordenada_inicio, coordenada_fim, G):
    # Encontra os nós mais próximos das coordenadas inicial e final
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    # Calcula o caminho mais curto entre os nós no grafo
    rota = nx.shortest_path(G, orig, dest, weight='length')
    # Plota o caminho no grafo em um mapa estático
    fig, ax = ox.plot_graph_route(G, rota)

# Função para plotar o caminho interativo entre duas coordenadas
def plotar_caminho_interativo(coordenada_inicio, coordenada_fim, G):
    # Encontra os nós mais próximos das coordenadas inicial e final
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    # Calcula o caminho mais curto entre os nós no grafo
    rota = nx.shortest_path(G, orig, dest, weight='length')
    # Converte o grafo em DataFrames de nós e arestas
    nodes, edges = ox.graph_to_gdfs(G)
    # Define o centro do mapa como a localização do primeiro nó
    centro = nodes.geometry.iloc[0].y, nodes.geometry.iloc[0].x
    # Cria um mapa interativo com Folium
    mapa = folium.Map(location=centro, zoom_start=13)
    # Adiciona o caminho ao mapa como uma linha
    rota_coords = [(nodes.loc[node].geometry.y, nodes.loc[node].geometry.x) for node in rota]
    folium.PolyLine(rota_coords, color="red", weight=2.5).add_to(mapa)
    # Salva o mapa interativo em um arquivo HTML
    mapa.save("caminho_interativo.html")
    print("Caminho interativo salvo como 'caminho_interativo.html'.")

# Função para plotar o caminho interativo entre dois endereços
def plotar_caminho_interativo_enderecos(endereco_inicio, endereco_fim, G):
    # Obtém as coordenadas dos endereços
    coordenada_inicio = obter_lat_lon(endereco_inicio)
    coordenada_fim = obter_lat_lon(endereco_fim)
    # Encontra os nós mais próximos das coordenadas inicial e final
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    # Calcula o caminho mais curto entre os nós no grafo
    rota = nx.shortest_path(G, orig, dest, weight='length')
    # Converte o grafo em DataFrames de nós
    nodes, _ = ox.graph_to_gdfs(G)
    # Define o centro do mapa como a localização do primeiro nó
    centro = nodes.geometry.iloc[0].y, nodes.geometry.iloc[0].x
    # Cria um mapa interativo com Folium
    mapa = folium.Map(location=centro, zoom_start=13)
    # Adiciona o caminho ao mapa como uma linha
    rota_coords = [(nodes.loc[node].geometry.y, nodes.loc[node].geometry.x) for node in rota]
    folium.PolyLine(rota_coords, color="red", weight=2.5).add_to(mapa)
    # Salva o mapa interativo em um arquivo HTML
    mapa.save("caminho_interativo_enderecos.html")
    print("Caminho interativo salvo como 'caminho_interativo_enderecos.html'.")

# Exemplo de uso
if __name__ == "__main__":
    # Carrega ou baixa o grafo do Centro de Fortaleza
    G = carregar_grafo()

    # Define os endereços de origem e destino
    endereco_inicio = "Rua Sena Madureira, Fortaleza, Ceará, Brasil"
    endereco_fim = "Rua Barão do Rio Branco, Fortaleza, Ceará, Brasil"

    # Plota o caminho interativo entre os dois endereços
    plotar_caminho_interativo_enderecos(endereco_inicio, endereco_fim, G)