# 정점 번호 / 상대 정점 번호 / 거리
# 3 1 2 4 3 -1 
# 정점3에서 1까지 거리 2
# 정점4에서 3까지 거리 3
# 마지막 -1

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    c = list(map(int, input().split()))
    for e in range(1, len(c)-2, 2):
        graph[c[0]].append((c[e], c[e+1]))