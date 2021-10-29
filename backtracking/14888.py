import sys
N = int(sys.stdin.readline().strip())

A = sys.stdin.readline().strip().split()
for i in range(len(A)):
    A[i] = int(A[i])

sum, sub, mul, div = map(int, sys.stdin.readline().strip().split())

# N = 4
# A = [2,3,4,5]
# sum, sub, mul, div = 2,1,0,0

# print (N,A)
# print (sum, sub, mul, div)
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

# print (arr)

# case = []
# ans = []

import itertools

case = list(itertools.permutations(arr,len(arr)))

# print (f'{type(result[0])}')
MAX = pow(10,9)*-1
MIN = pow(10,9)

# print (case)
# case = [['-','/','+','+','*'],['+','+','/','-','*']]
for c in case:
    temp_list = deque(copy.deepopy())


    res = 0

    if c[0] == '+':
        res = (A[0]+A[1])
    elif c[0] == '-':
        res = (A[0]-A[1])
    elif c[0] =='*':
        res = (A[0]*A[1])
    else:        
        res = A[0]//A[1]

    #맨처음 A[1] 연산 A[2]
    #두번째 위의 결과에 연산 A[3]
    #세번째 위의 결과에 연산 A[4]
    for i in range(1,len(c)): # 1,2,3 
        # print (f'{res = } {A[i+1]=} {c[i]=}')
        if c[i] == '+':
            res +=A[i+1]
        elif c[i] == '-':
            res -=A[i+1]
        elif c[i] =='*':
            res *=A[i+1]
        else:
            if res < 0:
                res = abs(res) // A[i+1]
                res *=-1
            else:
                res = res // A[i+1]
    
    MIN = min(MIN, res)
    MAX = max(MAX, res)

print (MAX, MIN)
