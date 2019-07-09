# 最小生成树

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    def weight(self):
        return self.weight

    def either(self):
        return self.v
    
    def other(self, v):
        return  self.w if v == self.v else self.v
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight
    
    def __eq__(self, other):
        return self.v == other.v and self.w == other.w
    
    def __hash__(self):
        return hash(str(self.v) + str(self.w))

    def __str__(self):
        return '(' + str(self.v) + '-' + str(self.w) + ')'

    __repr__ = __str__

class EdgeWeightedGraph:
    def __init__(self, n):
        self.list = [set() for i in range(n)]
        self.vertex_num = n
        self.edge_num = 0
    
    def add_edge(self, e:Edge):
        v = e.either()
        w = e.other(v)
        self.list[v].add(e)
        self.list[w].add(e)
        self.edge_num += 1
    
    def adj(self, v:int):
        return self.list[v]

    def vertex_num(self):
        return self.vertex_num
    
    def edge_num(self):
        return self.edge_num

    def edges(self):
        result = set()
        for v in range(self.vertex_num):
            for edge in self.adj(v):
                if edge.other(v) > v:
                    result.add(edge)
        return result
    
if __name__ == "__main__":
    g = EdgeWeightedGraph(10)
    g.add_edge(Edge(0, 1, 0.1))
    g.add_edge(Edge(1, 2, 0.2))