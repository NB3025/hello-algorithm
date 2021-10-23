# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다.(11, 13, 17, 19)
# 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

# 제한
# 1 ≤ n ≤ 123,456
# 예제 입력 1 
# 1 -> 1보다 크고, 2보다 작은 소수 
# 10
# 13 -> 13보다 크고 26보다 작거나 같은 소수
# 100
# 1000
# 10000
# 100000
# 0
# 예제 출력 1 
# 1
# 4
# 3
# 21
# 135
# 1033
# 8392

n = int(input())

def getPrimeCount(start,end):
    end+=1
    prime = [True] * end
    
    for i in range(2, int(end**0.5)+1):
        if prime[i]:
            for j in range(2*i, end, i):
                prime[j] = False
    
    ans = 0
    for i in range(start+1,end):
        if i>1 and prime[i]:
            # print (i)
            ans+=1
    print (ans)

while n != 0:
    start = n
    end = n*2
    if n ==1:
        print (1)
    else:
        getPrimeCount(start, end)
    
    n = int(input())
    
#     import sys
# import math

# input = sys.stdin.read


# def sol4948():
#     nm = 123456*2
#     nums = [1] * (nm+1)
#     nums[1] = 0
#     for i in range(2, int(math.sqrt(nm)) + 1):
#         if nums[i] == 1:
#             nums[i * 2::i] = [0] * (nm // i - 1)
#     answer = []
#     for m in map(int, input().split()):
#         if m == 0:
#             break
#         n = 2 * m
#         cnt = 0
#         if m <= 2 and n >= 2:
#             cnt += 1
#         cnt += sum(nums[m + 1 - m % 2:n+1:2])
#         answer.append(str(cnt - nums[m]))
#     print('\n'.join(answer))


# if __name__ == '__main__':
#     sol4948()