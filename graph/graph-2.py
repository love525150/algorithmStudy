# 列出连通集合
from queue import Queue

max = 10
num = 8
visited = [0 for i in range(num)]

def getGraph():
    graph = [[0 for i in range(max)] for j in range(max)]
    graph[0][7] = 1
    graph[7][0] = 1
    graph[0][1] = 1
    graph[1][0] = 1
    graph[2][0] = 1
    graph[0][2] = 1
    graph[0][2] = 1
    graph[4][1] = 1
    graph[1][4] = 1
    graph[2][4] = 1
    graph[4][2] = 1
    graph[3][5] = 1
    graph[5][3] = 1
    return graph

graph = getGraph()

def get_adjacent(vertex:int):
    result = []
    for i in range(max):
        if graph[vertex][i] == 1:
            result.append(i)
    return result

def dfs(vertex:int, mset:list):
    if visited[vertex]:
        return
    visited[vertex] = 1
    mset.append(vertex)
    for next_vertex in get_adjacent(vertex):
        dfs(next_vertex, mset)

def bfs(vertex:int, mset:list):
    if visited[vertex]:
        return
    visited[vertex] = 1
    mset.append(vertex)
    vertex_queue = Queue()
    for v in get_adjacent(vertex):
        vertex_queue.put(v)
    while not vertex_queue.empty():
        next_vertex = vertex_queue.get()
        if visited[next_vertex]:
            continue
        visited[next_vertex] = 1
        mset.append(next_vertex)
        for v in get_adjacent(next_vertex):
            vertex_queue.put(v)
    
    return mset

def find_next_unvisited():
    for index, visit in enumerate(visited):
        if visit == 0:
            return index

if __name__ == "__main__":
    msets = []
    v = find_next_unvisited()
    while v is not None:
        mset = []
        dfs(v, mset)
        msets.append(mset)
        v = find_next_unvisited()
    print("dfs:")
    print(msets)

    for i in range(len(visited)):
        visited[i] = 0
    
    msets = []
    v = find_next_unvisited()
    while v is not None:
        mset = []
        bfs(v, mset)
        msets.append(mset)
        v = find_next_unvisited()

    print("bfs:")
    print(msets)


