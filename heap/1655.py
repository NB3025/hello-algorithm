import sys
import heapq

input = sys.stdin.readline

N = int(input())

leftheap = []
rightheap = []
ans = []

for i in range(N):
    num = int(input())

    print (f'before {leftheap=}')
    if len(leftheap)==len(rightheap):
        heapq.heappush(leftheap, (-num, num))
    else:
        heapq.heappush(rightheap, (num, num))

    if rightheap and leftheap[0][1] > rightheap[0][0]:
        min = heapq.heappop(rightheap)[0]
        max = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-min, min))
        heapq.heappush(rightheap, (max, max))

    print (f'after {leftheap=}')
    ans.append(leftheap[0][1])

print (' '.join(map(str,ans)))