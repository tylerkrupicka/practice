# Route between nodes
# Given a directed graph, design an algo to find a route between two nodes.

def is_route(graph, a, b):
    # setup bfs
    seen = {}
    seen[a] = True
    q = [a]
    # perform bfs
    while(len(q) is not 0):
        cur = q.pop(0)
        if cur == b:
            return True # found route
        for node in graph[cur]:
            if node not in seen:
                seen[node] = True
                q.append(node)
    return False

if __name__ == '__main__':
    graph = {'A': ['C'],
        'B': ['C', 'D'],
        'C': ['D', 'E'],
        'D': ['C'],
        'E': ['F', 'A'],
        'F': ['C']}
    print(is_route(graph, 'A', 'E'))
