a = int(input())

for i in range(a):
    num = int(input())
    zero = [1,0]
    one = [0,1]
    
    if num == 0:
        print ('1 0')
    elif num ==1:
        print ('0 1')
    else:    
        for i in range(2, num+1): # 2,4
            zero.append(zero[i-1]+zero[i-2]) #zero1 +zero0
            one.append(one[i-1]+one[i-2]) #zero1+
        print (f'{zero[num]} {one[num]}')
    
