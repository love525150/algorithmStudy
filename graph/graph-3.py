# 六度空间
from queue import Queue


v_num = 10
visited = [0 for i in range(v_num)]
count = [0 for i in range(v_num)]
levels = [0 for i in range(v_num)]

def put_edge(v1:int, v2:int, graph):
    graph[v1].append(v2)
    graph[v2].append(v1)

def get_graph():
    graph = [[] for i in range(v_num)]
    for i in range(9):
        put_edge(i, i+1, graph)
    return graph

graph = get_graph()

def get_adjacent(v:int):
    return graph[v]

def clear_visited():
    for i in range(len(visited)):
        visited[i] = 0
        levels[i] = 0

def dfs(v:int, level:int):
    if visited[v] == 1:
        return
    visited[v] = 1
    level += 1
    print(str(v) + " is level " + str(level))
    for i in get_adjacent(v):
        dfs(i, level)

def bfs(v:int):
    v_queue = Queue()
    if visited[v] == 0:
        v_queue.put(v)
    while not v_queue.empty():
        next_vertex = v_queue.get()
        if visited[next_vertex]:
            continue
        visited[next_vertex] = 1
        print(str(next_vertex) + " is level " + str(levels[next_vertex]))
        count[v] += 1
        if levels[next_vertex] < 6:
            for j in get_adjacent(next_vertex):
                levels[j] = levels[next_vertex] + 1
                v_queue.put(j)
    
    clear_visited()


if __name__ == "__main__":
    bfs(0)
    bfs(1)
    bfs(2)
    bfs(3)
    bfs(4)
    bfs(5)
    bfs(6)
    bfs(7)
    bfs(8)
    bfs(9)
    print(count[0] / v_num)
    print(count[1] / v_num)
    print(count[2] / v_num)
    print(count[3] / v_num)
    print(count[4] / v_num)
    print(count[5] / v_num)
    print(count[6] / v_num)
    print(count[7] / v_num)
    print(count[8] / v_num)
    print(count[9] / v_num)