import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import folium
import os
import pickle
from shapely.geometry import Polygon, LineString, Point

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


# Função para plotar o caminho interativo entre duas coordenadas
def plotar_caminho_interativo(rota, geo_data):
    nodes = geo_data['nodes'] # Obtém os nós do grafo
    
    rota_nodes = nodes.loc[rota]  # Filtra os nós da rota    
    
    # Obtém os limites mínimos e máximos de latitude e longitude
    min_lat, max_lat = rota_nodes['y'].min(), rota_nodes['y'].max()
    min_lon, max_lon = rota_nodes['x'].min(), rota_nodes['x'].max()
    
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
    folium.PolyLine(rota_nodes[['y','x']].values, color="red", weight=2.5).add_to(mapa)
    
    # Adiciona marcadores para origem e destino
    folium.Marker(rota_nodes.iloc[0][['y','x']].values, popup="Origem").add_to(mapa)
    folium.Marker(rota_nodes.iloc[-1][['y','x']].values, popup="Destino").add_to(mapa)
    
    # Salva o mapa interativo em um arquivo HTML
    mapa.save("caminho_interativo.html")
    print("Caminho interativo salvo como 'caminho_interativo.html'.")

# Carregar dados geográficos
fortaleza = {}
fortaleza['G'] = carregar_grafo()
fortaleza['nodes'], fortaleza['edges'] = ox.graph_to_gdfs(fortaleza['G'])
fortaleza['bounds'] = fortaleza["nodes"].total_bounds


def nearest_node(coordinate, geo_data):
    """
    Encontra o nó mais próximo de uma coordenada dada.
    """
    nodes = geo_data['nodes']
    # Converte a coordenada para um ponto Shapely
    point = Point(coordinate[1], coordinate[0])  # (lon, lat)    
    # retorna o índice do nó mais próximo 
    # O Alerta que os dados precisam ser projetados para calcular a distância corretamente pode ser ignorado
    # pois estamos interessados em valor relativo e não absoluto
    return nodes.geometry.distance(point).idxmin() 



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
    
    node_origem = nearest_node(coordenada_inicio, fortaleza)
    node_destino = nearest_node(coordenada_fim, fortaleza)
    print(f"Nó de origem: {node_origem}")
    print(f"Nó de destino: {node_destino}")

    # Obter o caminho mais curto entre os nós
    rota = nx.shortest_path(fortaleza['G'], source=node_origem, target=node_destino, weight='length')    
    print(f"Caminho mais curto: {rota}")

    # Plotar o caminho interativo
    plotar_caminho_interativo(rota, fortaleza)