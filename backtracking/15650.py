import sys
N, M = map(int, sys.stdin.readline().strip().split())

ans = []

def bt():
    if len(ans) == M:
        print (' '.join(map(str,ans)))
        return
    for i in range(1, N+1):
        if i not in ans:
            if len(ans)==0:
                ans.append(i)
                bt()
                ans.pop()
            else:
                if i>ans[-1]:
                    ans.append(i)
                    bt()
                    ans.pop()


bt()