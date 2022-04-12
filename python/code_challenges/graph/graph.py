


class Graph:

    def __init__(self):
        self.nodes = dict()
        self.edges = dict()


    def add_node(self, value):

        if value not in self.nodes:
            # init node with no neighbors
            self.nodes[value] = list()

    def add_edge(self, node1, node2, weight=None):

        if node1 in self.nodes and node2 in self.nodes:
            # adding edge both ways for undirected graph
            edge_forward = (node1, node2)
            edge_back = (node2, node1)

            # set weight for edge 
            self.edges[edge_forward] = weight
            self.edges[edge_back] = weight

            # add both nodes to list of neighbors
            self.nodes[node1].append(node2)
            self.nodes[node2].append(node1)


    def get_nodes(self):
        if len(self.nodes):
            return sorted(list(self.nodes.keys()))
        else:
            return None

    def get_neighbors(self, node):
        if node not in self.nodes:
            return None
        res = []
        for nei in sorted(self.nodes[node]):
            res.append((nei, self.edges[(node,nei)]))
        return res

    def size(self):
        return len(self.nodes)

    def breadth_first(self, node=None):
        if not node: return []
        res = []
        seen = {node}
        queue = [node]

        while queue:
            node = queue.pop(0)
            res.append(node)

            for neighbor in sorted(self.nodes[node]):
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
        
        return res

    def depth_first(self, node=None):
        if not node or node not in self.nodes: return []

        res = []
        stack = [node]
        seen = set()

        while stack:
            curnode = stack.pop()
            res.append(curnode)
            if curnode not in seen:
                seen.add(curnode)
                for neighbor in reversed(self.nodes[curnode]):
                    if neighbor not in seen:
                        stack.append(neighbor)

        return res

            
    def business_trip(self, cities):
        if not cities: return None
        
        cost = 0

        for i in range(len(cities)-1):
            trip = (cities[i], cities[i+1])

            if trip in self.edges:
                cost += self.edges[trip]
            else:
                return None
        
        return cost


    def __str__(self):
        for node, neighbors in self.nodes:
            if neighbors:
                for nei in neighbors:
                    print('(' + node + ') -> (' + nei + '), weight = ' + self.edges[(node, nei)])
            else:
                print('(' + node + ')')


