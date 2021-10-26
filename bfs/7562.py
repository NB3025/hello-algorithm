import sys
from collections import deque


N = int(sys.stdin.readline())
for _ in range(N):
    l = int(sys.stdin.readline())

    graph = [[0]*l for _ in range(l)]

    x1,y1 = map(int, sys.stdin.readline().strip().split())
    x2,y2 = map(int, sys.stdin.readline().strip().split())

    queue = deque([])

    dx = [1,2,1,2,-1,-2,-1,-2]
    dy = [2,1,-2,-1,-2,-1,2,1]

    queue.append([x1,y1])
    while queue:
        x,y = queue.popleft()

        if x==x2 and y==y2:
            print (graph[x][y])
            break
        else:
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<l and 0<=ny<l and graph[nx][ny]==0:
                    queue.append([nx,ny])
                    graph[nx][ny] = graph[x][y]+1

