import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

def bfs(x, mode):
    q = deque()
    q.append(x)
    c = [-1 for _ in range(N)]
    c[x] = 0
    while q:
        x = q.popleft()
        for w, nx in A[x]:
            if c[nx] == -1:
                c[nx] = c[x] + w
                q.append(nx)
    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)

A = [[] for _ in range(N)]

for i in range(N-1):
    x, y, w = map(int, input().split())
    A[x-1].append([w, y-1])
    A[y-1].append([w, x-1])

print (bfs(bfs(0,1),2))