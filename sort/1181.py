import sys

N = int(sys.stdin.readline())
A = []

for _ in range(N):
    A.append(sys.stdin.readline().strip())

set_A = set(A)
A = list(set_A)

A.sort()
A.sort(key=len)

for i in A:
    print (i)