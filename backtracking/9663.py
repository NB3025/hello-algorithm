




#https://rebas.kr/761
import sys
N = int(sys.stdin.readline().strip())

def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
            return False
    return True


def dfs(x):
    global res
    if x == N:
        res += 1
        return
    for i in range(N):
        col[x] = i
        if check(x):
            dfs(x+1)

res = 0
col = [0]*15

dfs(0)
print (res)