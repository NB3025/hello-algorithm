def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i]==1 and visited[i] == 0:
                    stack.append(i)
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer


# 1,1 / 2,2 /3,3 은 항상 1이고
# 1,2 연결 2,1연결, 3연결 없음
# [1, 1, 0]
# [1, 1, 0]
# [0, 0, 1]

n1 = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n2 = 3
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print (solution(n1, computers1))

print (solution(n2, computers2))

