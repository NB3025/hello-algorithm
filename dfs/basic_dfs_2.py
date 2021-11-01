import sys

input = sys.stdin.readline
N = int(input())

visited = [0] * (N+1)

graph = []
for _ in range(N):
    graph.append(list(input().strip()))


def dfs(V):
    visited[V] = 1
    print ('V',end=' ')
    for i in range(1,N+1):
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)
            
            