import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    #시작 노드 초기화
    dist[start] = 0

    #전체 n번의 라운드 반복
    for i in range(N):
        # 매 반복마다 모든 간선 확인
        for j in range(M):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짦으면
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신되면 음수 순환이 존재한다.
                if i == n - 1:
                    return True
    return False

N, M = map(int, input().split())
# 모든 간선에 대한 정보 리스트
edges = []
# 최단 거리 테이블 모두 무한으로 초기화
dist = [INF] * (N+1)

#간선정보 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a,b,c,))

negative_cycle = bf(1)

if negative_cycle:
    print (-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print (-1)
        else:
            print (dist[i])