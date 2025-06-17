import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [
        (cost, start, to)
        for to, cost in graph[start].items()
    ]
    heapq.heapify(edges)
    
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost2 in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost2, to, to_next))
    return mst

# Ejemplo de grafo (nodo: {nodo_vecino: peso})
graph = {
    'A': {'B': 2, 'D': 6},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'B': 3, 'D': 4, 'E': 2},
    'D': {'A': 6, 'B': 8, 'C': 4, 'E': 1},
    'E': {'C': 2, 'D': 1}
}

mst = prim(graph, 'A')
print("Aristas del MST (Prim):")
for frm, to, cost in mst:
    print(f"{frm} -- {to} (Peso: {cost})")