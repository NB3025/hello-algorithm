import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split())
queue = deque([M])

MAX=10**5
dist = [0]*(MAX+1)

def bfs():   
    while queue:
        v=queue.popleft()
        if N == v:
            print (dist[v])
            break
        for nx in (v-1, v+1, v*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[v]+1
                queue.append(nx)
                
bfs()