import sys
N, M = map(int, sys.stdin.readline().strip().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))


print (M,N,graph)

dx,dy = [-1,+1,0,0], [0,0,-1,+1]
def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    
    print (f'{x=}{y=}')
    if graph[x][y]==0:
        graph[x][y]=2
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        
for i in range(N):
    for j in range(M):
        dfs(i,j)
print (M,N,graph)

# [2, 1, 2, 2], 
# [1, 1, 1, 2], 
# [1, 2, 2, 2], 
# [2, 2, 2, 2], 
# [2, 1, 1, 1], 
# [2, 2, 2, 2]