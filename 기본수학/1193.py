# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

# 예제 입력 1 
# 1
# 예제 출력 1 
# 1/1
# 예제 입력 2 
# 2
# 예제 출력 2 
# 1/2
# 예제 입력 3 
# 3
# 예제 출력 3 
# 2/1
# 예제 입력 4 
# 4
# 예제 출력 4 
# 3/1
# 예제 입력 5 
# 5
# 예제 출력 5 
# 2/2
import sys
input = int(sys.stdin.readline())

count = 1
for i in range(2,10000000):
    if input <=count:
        # print (f'i = {i} /(i-1)-(input-count) = {(i-1)-(count-input)}')
        a = (i-1)-(count-input)
        if i%2==0:
            print (f'{(i-a)}/{a}')
        else:
            print (f'{(a)}/{i-a}')
        break
    count +=i

    