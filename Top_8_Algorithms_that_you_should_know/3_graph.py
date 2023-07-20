## 3. Graph Algorithm:
## Dijkstra's shortest path algorithn: Dijkstra's shortest path algorithm is an algorithm for finding the shortest path between nodes in a graph.

import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()

    while heap:
        (cost, v) = heapq.heappop(heap)
        if v not in visited:
            visited.add(v)
            for u, c in graph[v].items():
                if u not in visited:
                    heapq.heappush(heap, (cost + c, u))

    return visited


graph = {
    'A' : {'B': 2, 'C' : 3},
    'B' : {'D': 4, 'E' : 5},
    'C' : {'F' : 6},
    'D' : {'G' : 7},
    'E' : {'G' : 8, 'H' : 9},
    'F' : {'H' : 10},
    'G' : {},
    'H' : {}
}


print (dijkstra(graph, 'A'))
