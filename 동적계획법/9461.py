import sys

T = int(sys.stdin.readline())

arr = [0] * 100
arr[0] = 1
arr[1] = 1
arr[2] = 1
arr[3] = 2
arr[4] = 2
arr[5] = 3

for i in range(6, 100):
    arr[i] = arr[i - 2] + arr[i - 3]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(arr[N - 1])
