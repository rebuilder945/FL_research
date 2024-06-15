def calDegrees(lt):
 
    index1 = 0                      
 
    max = 0                          
 
    for i in range(len(lt)):
 
        flag = 0                  
 
        for j in range(i+1,len(lt)): 
 
            if lt[j] == lt[i]:
 
                flag += 1         
 
        if flag > max:           
            max = flag
            index1 = i
 
    return lt[index1]


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

