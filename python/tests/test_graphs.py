import pytest
from code_challenges.graph.graph import Graph



def test_add_node_to_graph():
    graph = Graph()
    graph.add_node(5)

    expected = [5]
    actual = graph.get_nodes()
    assert expected == actual

def test_add_edge_to_graph():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1,2)

    expected = [2]
    actual = graph.nodes[1]
    return expected == actual


def test_get_all_nodes():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    expected = [1,2,3,4,5]
    actual = graph.get_nodes()
    assert expected == actual

def test_get_neighbors_from_graph():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)

    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    
    # Get neighbors of node 1
    expected = [(2, None), (3, None), (4, None)]
    actual = graph.get_neighbors(1)
    assert expected == actual

def test_get_edges_of_neighbors_with_weight():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(5)

    graph.add_edge(1,2, 100)
    graph.add_edge(2,3, 25)
    graph.add_edge(5,2,10)

    expected = [(1,100), (3,25), (5,10)]
    actual = graph.get_neighbors(2)
    assert expected == actual

    
def test_get_size_of_graph():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    expected = 5
    actual = graph.size()
    assert expected == actual
    
def test_empty_graph_returns_null():
    graph = Graph()

    assert graph.get_nodes() == None
    assert graph.get_neighbors(1) == None
