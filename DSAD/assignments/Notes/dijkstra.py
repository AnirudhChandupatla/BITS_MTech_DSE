from queue import PriorityQueue
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v: {'dist':float('inf'),'prev':[]} for v in range(graph.v)}
    D[start_vertex] = {'dist':0,'prev':start_vertex}

    pq = PriorityQueue()
    pq.put((0, start_vertex))
    
    while not pq.empty():
        print('-'*10)
        print('visited: ',graph.visited)
        print('Q: ',sorted(pq.queue,key=lambda x:x[0]))
        (dist, current_vertex) = pq.get()
        print('get: ', (dist, current_vertex))
        print('Q: ',sorted(pq.queue,key=lambda x:x[0]))
        graph.visited.append(current_vertex)
        print('visited: ',graph.visited)
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]['dist']
                    new_cost = D[current_vertex]['dist'] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        print('Put: ', (new_cost, neighbor))
                        D[neighbor]['dist'] = new_cost
                        D[neighbor]['prev'] = current_vertex
        print('Q: ',sorted(pq.queue,key=lambda x:x[0]))
    return D


if __name__ == '__main__':
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 8, 2)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    D = dijkstra(g, 0)

    print(D)

    for vertex in range(len(D)):
        print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])