def shift_list(n):  
    # 生成列表 [1, 2, ... , n-1, n]  
    list_nums = list(range(1, n+1))  
      
    # 循环左移列表  
    for i in range(len(list_nums)):  
        list_nums.append(list_nums.pop(0))  
      
    return list_nums  
  
n = int(input())  
print(shift_list(n))
