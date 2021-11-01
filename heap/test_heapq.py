import heapq

N = [3,6,1,8,2,4,11,9]
heap = []

for i in N:

    heapq.heappush(heap, i)
    print (f'{heap=}')
