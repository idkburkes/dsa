from re import L
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

def test_breadth_first(sample_graph):
    expected = ['pandora', 'arendelle', 'metroville', 'monstropolis', 'naboo', 'narnia']
    actual = sample_graph.breadth_first('pandora')
    assert expected == actual 

def test_bfs_empty_graph():
    empty_graph = Graph()
    actual = empty_graph.breadth_first()
    expected = []
    assert actual == expected

def test_business_trip_2_cities(weighted_graph):
    cities = ['metroville', 'pandora']
    actual = weighted_graph.business_trip(cities)
    expected = 82
    assert actual == expected

def test_business_trip_3_cities(weighted_graph):
    cities = ['arendelle', 'monstropolis', 'naboo']
    actual = weighted_graph.business_trip(cities)
    expected = 115
    assert actual == expected

def test_business_trip_2_cities_trip_not_possible(weighted_graph):
    cities = ['naboo', 'pandora']
    actual = weighted_graph.business_trip(cities)
    expected = None
    assert actual == expected

def test_business_trip_3_cities_trip_not_possible(weighted_graph):
    cities = ['narnia', 'arendelle', 'naboo']
    actual = weighted_graph.business_trip(cities)
    expected = None
    assert actual == expected

def test_depth_first(sample_graph2):
    actual = sample_graph2.depth_first('A')
    expected = ['A','B','C','G','D','E','H','F']
    print(actual)
    print(expected)
    assert actual == expected




@pytest.fixture
def sample_graph():
    graph = Graph()

    #Pandora, Arendelle, Metroville, Monstroplolis, Narnia, Naboo
    graph.add_node('pandora')
    graph.add_node('arendelle')
    graph.add_node('metroville')
    graph.add_node('monstropolis')
    graph.add_node('narnia')
    graph.add_node('naboo')

    graph.add_edge('pandora', 'arendelle')
    graph.add_edge('arendelle', 'metroville')
    graph.add_edge('arendelle', 'monstropolis')
    graph.add_edge('metroville', 'monstropolis')
    graph.add_edge('metroville', 'naboo')
    graph.add_edge('metroville', 'narnia')
    graph.add_edge('monstropolis', 'naboo')
    graph.add_edge('naboo', 'narnia')
    
    return graph

@pytest.fixture
def sample_graph2():
    graph = Graph()

    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_node('G')
    graph.add_node('H')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'G')
    graph.add_edge('D', 'E')
    graph.add_edge('D', 'H')
    graph.add_edge('D', 'F')

    return graph

@pytest.fixture
def weighted_graph():
    graph = Graph()

    #Pandora, Arendelle, Metroville, Monstroplolis, Narnia, Naboo
    graph.add_node('pandora')
    graph.add_node('arendelle')
    graph.add_node('metroville')
    graph.add_node('monstropolis')
    graph.add_node('narnia')
    graph.add_node('naboo')

    graph.add_edge('pandora', 'arendelle', 150)
    graph.add_edge('pandora', 'metroville', 82)
    graph.add_edge('arendelle', 'metroville', 99)
    graph.add_edge('arendelle', 'monstropolis', 42)
    graph.add_edge('metroville', 'monstropolis', 105)
    graph.add_edge('metroville', 'naboo', 26)
    graph.add_edge('metroville', 'narnia', 37)
    graph.add_edge('monstropolis', 'naboo', 73)
    graph.add_edge('naboo', 'narnia', 250)

    return graph


    




