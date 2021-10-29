from collections import Counter
import sys

N = int(sys.stdin.readline())
A = []

for _ in range(N):
    A.append(int(sys.stdin.readline()))


A.sort()

print (round(sum(A)/len(A)))
print (A[len(A)//2])

cnt = Counter(A).most_common(2)

if len(A) >1:
    if cnt[0][1] == cnt[1][1]:
        print (cnt[1][0])
    else:
        print (cnt[0][0])
else:
    print (cnt[0][0])

print (max(A)-min(A))