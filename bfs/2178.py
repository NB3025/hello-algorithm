import sys

N, M = map(int, sys.stdin.readline().strip().split())

graph = [list(map(int, input())) for _ in range(N)]

queue =[]
queue = [[0,0]]

dx,dy = [1,-1,0,0], [0,0,-1,1]

graph[0][0]=1


while queue:
    x,y = queue[0][0], queue[0][1]
    
    del queue[0]
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
            queue.append([nx,ny])
            graph[nx][ny]=graph[x][y]+1

print (graph)

