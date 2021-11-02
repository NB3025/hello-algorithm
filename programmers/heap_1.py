import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def sol(scoville, K):
    count = 0
    
    # 아래 수식을 반복하며 min이 K보다 큰지 검사함
    # scovile[0] = scoville[0] + (scoville[1]*2) 
    
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap)+(heapq.heappop(heap)*2))
        except IndexError:
            return -1
        count +=1

    return count

print (sol(scoville,K))