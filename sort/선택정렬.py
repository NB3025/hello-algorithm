# 제일 첫번째 요소를 선택하고
# 두번째부터 마지막까지 검사를 한다.
# 두번째부터 마지막까지의 요소 중 가장 작은 요소의 값을 찾고
# 제일 첫번째 요소와 위치 변경

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 변경

print (array)

# 