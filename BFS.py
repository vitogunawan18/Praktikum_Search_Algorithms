import collections

# BFS algorithm
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    traversal = [] 
    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        traversal.append(vertex)  

        # If not visited, mark it as visited, and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    # Cetak hasil traversal dalam urutan terbalik
    print(" ".join(map(str, traversal[::-1])))  # Membalik list sebelum mencetak

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal (Reversed): ")
    bfs(graph, 0)