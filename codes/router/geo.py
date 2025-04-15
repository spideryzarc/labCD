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
GRAFO_PATH = "fortaleza.pkl"

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
        G = ox.graph_from_place("Fortaleza, Ceará, Brasil", network_type='drive')
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
def distancia_via(coordenada_inicio, coordenada_fim, geo_data):
    G = geo_data['G'] # Obtém o grafo do dicionário
    # Encontra os nós mais próximos das coordenadas inicial e final
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    # Calcula a distância mais curta entre os nós no grafo
    distancia = nx.shortest_path_length(G, orig, dest, weight='length')
    return distancia

# Função para plotar o caminho estático entre duas coordenadas
def plotar_caminho(coordenada_inicio, coordenada_fim, geo_data):
    G = geo_data['G'] # Obtém o grafo do dicionário
    # Encontra os nós mais próximos das coordenadas inicial e final
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    # Calcula o caminho mais curto entre os nós no grafo
    rota = nx.shortest_path(G, orig, dest, weight='length')
    # Plota o caminho no grafo em um mapa estático
    fig, ax = ox.plot_graph_route(G, rota)

# Função para plotar o caminho interativo entre duas coordenadas
def plotar_caminho_interativo(coordenada_inicio, coordenada_fim, geo_data):
    G = geo_data['G'] # Obtém o grafo do dicionário
    nodes = geo_data['nodes'] # Obtém os nós do grafo
    # Encontra os nós mais próximos das coordenadas inicial e final
    orig = ox.nearest_nodes(G, coordenada_inicio[1], coordenada_inicio[0])
    dest = ox.nearest_nodes(G, coordenada_fim[1], coordenada_fim[0])
    # Calcula o caminho mais curto entre os nós no grafo
    rota = nx.shortest_path(G, orig, dest, weight='length')
    
    
    # Extrai as coordenadas dos nós na rota
    rota_coords = [(nodes.loc[node].geometry.y, nodes.loc[node].geometry.x) for node in rota]
    
    # Calcula os limites (bounds) da rota
    lats = [coord[0] for coord in rota_coords]
    lons = [coord[1] for coord in rota_coords]
    min_lat, max_lat = min(lats), max(lats)
    min_lon, max_lon = min(lons), max(lons)
    
    # Adiciona uma pequena margem para melhor visualização
    margem = 0.001  # aproximadamente 100m
    min_lat -= margem
    max_lat += margem
    min_lon -= margem
    max_lon += margem
    
    # Cria um mapa interativo com Folium
    mapa = folium.Map()
    
    # Ajusta o mapa para os limites da rota
    mapa.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])
    
    # Adiciona o caminho ao mapa como uma linha
    folium.PolyLine(rota_coords, color="red", weight=2.5).add_to(mapa)
    
    # Adiciona marcadores para origem e destino
    folium.Marker(rota_coords[0], popup="Origem").add_to(mapa)
    folium.Marker(rota_coords[-1], popup="Destino").add_to(mapa)
    
    # Salva o mapa interativo em um arquivo HTML
    mapa.save("caminho_interativo.html")
    print("Caminho interativo salvo como 'caminho_interativo.html'.")



# Carregar dados geográficos
fortaleza = {}
fortaleza['G'] = carregar_grafo()
fortaleza['nodes'], fortaleza['edges'] = ox.graph_to_gdfs(fortaleza['G'])
fortaleza['bounds'] = fortaleza["nodes"].total_bounds


# Exemplo de uso
if __name__ == "__main__":
   

    # Define os endereços de origem e destino
    endereco_inicio = "Rua Sena Madureira, Fortaleza, Ceará, Brasil"
    endereco_fim = "Rua Barão do Rio Branco, Fortaleza, Ceará, Brasil"

    # Obtém as coordenadas dos endereços
    coordenada_inicio = obter_lat_lon(endereco_inicio)
    coordenada_fim = obter_lat_lon(endereco_fim)
    print(f"Coordenada de início: {coordenada_inicio}")
    print(f"Coordenada de fim: {coordenada_fim}")

    # Calcula a distância viária entre os endereços
    distancia = distancia_via(coordenada_inicio, coordenada_fim, fortaleza)
    print(f"Distância viária: {distancia} metros")
    # Plota o caminho estático entre os endereços
    # plotar_caminho(coordenada_inicio, coordenada_fim, G)
    # Plota o caminho interativo entre os endereços
    plotar_caminho_interativo(coordenada_inicio, coordenada_fim, fortaleza)