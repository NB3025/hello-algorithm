import sys

input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range (N+1)]
visited= []*(N+1)

def dfs(graph, v, visited):
    visited[v] = True
    print (v, end=' ')
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)
