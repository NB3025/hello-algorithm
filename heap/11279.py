import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    # if num != 0:
    heapq.heappush(heap,(-num))
    # else:
        # try:
            # print (-1*heapq.heappop(heap))
        # except:
            # print (0)

for _ in range(len(heap)):
    print (heapq.heappop(heap))
