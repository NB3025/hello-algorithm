import sys
N, M = map(int, sys.stdin.readline().strip().split())

ans = []

def bt(idx):
    if len(ans)==M:
        print (' '.join(map(str,ans)))
        return
    for i in range(idx,N+1):
        ans.append(i)
        bt(i)
        ans.pop()
        
bt(1)