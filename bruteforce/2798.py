import sys

N, M = map(int, sys.stdin.readline().strip().split())

# arr = []
# arr = int(sys.stdin.readline().strip().split)
arr = list(map(int, input().split()))

arr.sort(reverse=True)

s_index = 0
for i in range(len(arr)):
    if M<arr[i]:
        s_index+=1
    else:
        break

print (arr)
print (s_index)
for i in range(s_index,len(arr)-2):
    sum = arr[i]+arr[i+1]+arr[i+2]
    if sum <=M:
        print (sum)
        break

