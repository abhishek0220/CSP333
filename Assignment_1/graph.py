class Graph:
    def __init__(self, graph_dict={}, directed=True):
        self.graph_dict = graph_dict
        self.directed = directed
        if( not self.directed ):
            self.make_undirected()
    
    def make_undirected(self):
        self.directed = False
        for a in self.graph_dict:
            for (b,dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    
    def connect(self, a, b, dist):
        self.graph_dict.setdefault(a, {})[b] = dist
        if(not self.directed):
            self.graph_dict.setdefault(b, {})[a] = dist
    
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def all_nodes(self):
        s = set()
        for a in self.graph_dict:
            s.add(a)
            for b in self.graph_dict[a]:
                s.add(b)
        return list(s)