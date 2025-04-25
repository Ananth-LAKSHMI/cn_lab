import matplotlib.pyplot as plt
import networkx as nx

def draw_distance_vector_topology():
    # Create graph
    G = nx.Graph()

    # Add nodes (routers)
    routers = ['1', '2', '3', '4']
    G.add_nodes_from(routers)

    # Add edges with weights (costs)
    edges = [
        ('1', '2', 2),
        ('1', '4', 1),
        ('2', '3', 3),
        ('3', '4', 4)
    ]
    G.add_weighted_edges_from(edges)

    # Define positions for layout
    positions = {
        '1': (0, 1),
        '2': (-1, 0),
        '3': (0, -1),
        '4': (1, 0)
    }

    # Draw nodes
    nx.draw_networkx_nodes(G, pos=positions, node_color='skyblue', node_size=1000)

    # Draw edges with widths
    nx.draw_networkx_edges(G, pos=positions, width=2)

    # Draw labels for routers
    nx.draw_networkx_labels(G, pos=positions, font_size=12, font_weight='bold')

    # Draw edge labels (costs)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels, font_size=11)

    plt.title("Distance Vector Routing Topology", fontsize=14)
    plt.axis('off')
    plt.show()

draw_distance_vector_topology()
