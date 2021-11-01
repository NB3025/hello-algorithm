from collections import deque
import sys

def bfs(graph, start, visited):
    queue = deque([start])
    #현재 노드 방문 처리
    visited[start] = True
    #큐가 있는동안 반복
    while queue:
        #큐에서 하나의 원소 출력
        v = queue.popleft()
        print (v, end=' ')
        #아직 방문하지 않은 인접한 원소 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

input = sys.stdin.readline
N = int(input())
visited = [False] *(N+1)
graph = []
for _ in range(N):
    graph.append(list(input().strip()))
