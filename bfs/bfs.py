from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v=queue.popleft()
        print (v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                

def bfs(V):
    queue=[V]
    visited[V] = 0
    while queue:
        V=queue.pop(0)
        print (V, end=' ')
        for i in range(1, N+1):
            if visited[i]==1 and graph[V][i]==1:
                queue.append(i)
                visited[i]=0
    