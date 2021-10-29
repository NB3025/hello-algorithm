import sys
N = int(sys.stdin.readline().strip())

A = sys.stdin.readline().strip().split()

sum, sub, mul, div = map(int, sys.stdin.readline().strip().split())

print (N,A)
print (sum, sub, mul, div)
arr = []
M = 0
for _ in range(sum):
    M +=1
    arr.append('+')

for _ in range(sub):
    M +=1
    arr.append('-')

for _ in range(mul):
    M +=1
    arr.append('*')

for _ in range(div):
    M +=1
    arr.append('/')

print (arr)

case = []

ans = []
def bt():
    if len(ans) == M:
        case.append(ans)
        print (f'{ans=}')
        return
    
    for n in arr:
        if n not in ans:
            ans.append(n)
            bt()
            ans.pop
        
bt()

print (case)
