import sys
N, M = map(int, sys.stdin.readline().strip().split())

ans = []

def bt():
    # A,b = map(int, sys.stdin.readline().strip().split())
    # print (f'{ans=} {len(ans)=} {M=}')
    if len(ans)==M:
        print (' '.join(map(str,ans)))
        return
    for i in range(1,N+1):
        # if i not in ans:
        ans.append(i)
        bt()
        ans.pop()

bt()