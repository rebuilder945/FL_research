def max_number(num_list):
    if not num_list:
        return 0
    count=[0]*10
    for num in num_list:
        count[num]+=1
    result=0
    for i in range(9,-1,-1):
        while count[i]>0:
            result=result*10+i
            count[i]-=1
    return result
input_str=input()
num_list=list(map(int,input_str.split(',')))
print(max_number(num_list))
        
