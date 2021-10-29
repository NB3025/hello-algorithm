import sys

N = int(sys.stdin.readline())
A = list(map(int, input().split()))

stack = []
ans = [-1 for _ in range(N)]


# 큰 수 중 가장 먼저 나오는 것을 넣어야 하기 때문에!
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

for r in ans:
    print (r,end=' ')