import igraph as ig
import matplotlib.pyplot as plt
from world_cups import all_plays, all_results


teams_ref = {'HOL': 0, 'CRO': 1, 'CNO': 2, 'PER': 3, 'HON': 4, 'MAR': 5, 'GAL': 6, 'PAR': 7, 'JAP': 8, 'AUS': 9, 'CRC': 10, 
'SUI': 11, 'CMR': 12, 'SER': 13, 'NZE': 14, 'ESP': 15, 'ISL': 16, 'FRA': 17, 'BOS': 18, 'IRA': 19, 'ARG': 20, 'ING': 21, 
'AFS': 22, 'CAN': 23, 'ITA': 24, 'EGI': 25, 'CAT': 26, 'SEN': 27, 'TUN': 28, 'EUA': 29, 'POR': 30, 'POL': 31, 'GRE': 32, 
'ESL': 33, 'URU': 34, 'COL': 35, 'PAN': 36, 'CDM': 37, 'EQU': 38, 'BEL': 39, 'AGL': 40, 'CHI': 41, 'DIN': 42, 'NIG': 43, 
'COR': 44, 'CAM': 45, 'RUS': 46, 'ARS': 47, 'GAN': 48, 'BRA': 49, 'ALE': 50, 'SUE': 51, 'MEX': 52, 'EVQ': 53
}

def generate_edges(directed):
    edges = []
    for index, play in enumerate(all_plays):
        if isinstance(all_results[index][2], int):

            winner_index = all_results[index][2]
            loser_index = 1 - winner_index
            edges.append(
                (
                    teams_ref[play[loser_index]],
                    teams_ref[play[winner_index]]
                )
            )

        else:
            continue
            '''edges.append(
                (
                    teams_ref[play[0]]
                    , teams_ref[play[1]]
                )
            )

            if directed:
                edges.append(
                    (
                        teams_ref[play[1]]
                        , teams_ref[play[0]]
                    )
                )'''
            
    return edges

def generate_graph(directed=False):
    edges = generate_edges(directed=directed)
    g = ig.Graph(n=len(teams_ref), edges=edges, directed=directed)
    return g

def plot_graph(g, fig_name):
    g["title"] = "World Cup Network"
    g.vs["team"] = list(teams_ref.keys())
    g.vs["color"] = ["yellow"] * len(teams_ref)

    fig, ax = plt.subplots(figsize=(20,20))
    ig.plot(
        g,
        target=ax,
        vertex_label=g.vs["team"],
        vertex_label_size=13,
        vertex_size=0.5
    )

    fig.savefig(fig_name)
    plt.show()

def get_pagerank_metric(g=generate_graph(directed=True)):
    pagerank = g.pagerank()
    pagerank_values = {}

    for i, v in enumerate(pagerank):
        pagerank_values[i] = v

    plot_graph(g, "pagerank_graph.png")

    return list(dict(sorted(pagerank_values.items(), key=lambda item: item[1], reverse=True)).keys())

def get_eigenvector_metric(g=generate_graph()):
    eigenvector = g.evcent()
    eigenvector_values = {}

    for i, v in enumerate(eigenvector):
        eigenvector_values[i] = v

    plot_graph(g, "eigenvector_graph.png")

    return list(dict(sorted(eigenvector_values.items(), key=lambda item: item[1], reverse=True)).keys())
    

print(get_pagerank_metric())
#print()
#print(get_eigenvector_metric())

