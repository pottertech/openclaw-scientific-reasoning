#!/usr/bin/env python3
"""NetworkX wrapper template for OpenClaw-Scientific-Reasoning.

This template demonstrates how to analyze graphs using NetworkX.
"""

import networkx as nx
import json


def analyze_graph(graph_data):
    """Analyze a graph structure.
    
    Args:
        graph_data: Dict with nodes and edges
    
    Returns:
        dict with analysis results
    """
    # Create graph from data
    G = nx.Graph()
    
    # Add nodes
    for node in graph_data.get('nodes', []):
        G.add_node(node['id'], **node.get('attributes', {}))
    
    # Add edges
    for edge in graph_data.get('edges', []):
        G.add_edge(edge['source'], edge['target'], **edge.get('attributes', {}))
    
    # Analyze
    results = {
        'node_count': G.number_of_nodes(),
        'edge_count': G.number_of_edges(),
        'is_connected': nx.is_connected(G) if len(G) > 0 else False,
        'components': list(nx.connected_components(G)),
        'component_count': nx.number_connected_components(G)
    }
    
    # Centrality (if graph is not empty)
    if len(G) > 0:
        try:
            results['degree_centrality'] = nx.degree_centrality(G)
            results['betweenness_centrality'] = nx.betweenness_centrality(G)
        except:
            pass
    
    return results


def find_critical_nodes(graph_data):
    """Find critical nodes in the graph.
    
    Critical nodes are those with highest betweenness centrality
    or whose removal would disconnect the graph.
    
    Args:
        graph_data: Dict with nodes and edges
    
    Returns:
        dict with critical node analysis
    """
    G = nx.Graph()
    
    for node in graph_data.get('nodes', []):
        G.add_node(node['id'])
    
    for edge in graph_data.get('edges', []):
        G.add_edge(edge['source'], edge['target'])
    
    if len(G) == 0:
        return {'error': 'Empty graph'}
    
    # Find articulation points (cut vertices)
    try:
        articulation_points = list(nx.articulation_points(G))
    except:
        articulation_points = []
    
    # Find nodes with highest centrality
    try:
        betweenness = nx.betweenness_centrality(G)
        top_nodes = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]
    except:
        top_nodes = []
    
    return {
        'articulation_points': articulation_points,
        'high_centrality_nodes': [{'node': n, 'centrality': c} for n, c in top_nodes],
        'critical_node_count': len(articulation_points)
    }


def main():
    """Example usage."""
    # Example: Simple service dependency graph
    graph_data = {
        'nodes': [
            {'id': 'api-gateway'},
            {'id': 'auth-service'},
            {'id': 'user-service'},
            {'id': 'database'}
        ],
        'edges': [
            {'source': 'api-gateway', 'target': 'auth-service'},
            {'source': 'api-gateway', 'target': 'user-service'},
            {'source': 'auth-service', 'target': 'database'},
            {'source': 'user-service', 'target': 'database'}
        ]
    }
    
    results = analyze_graph(graph_data)
    print(json.dumps(results, indent=2))
    
    critical = find_critical_nodes(graph_data)
    print("\nCritical nodes:")
    print(json.dumps(critical, indent=2))


if __name__ == '__main__':
    main()
