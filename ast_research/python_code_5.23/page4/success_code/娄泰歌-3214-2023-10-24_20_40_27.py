move_zeros_to_end = input()
def move_zeros_to_end(lst):  
    # 初始化两个指针  
    i = 0  
    j = len(lst) - 1  
  
    # 当i不越界时循环执行  
    while i < j:  
        # 如果lst[i]等于0，将i向后移动一位并将j位置替换为0  
        if lst[i] == 0:  
            lst[i] = 0  
            lst[j] = 0  
            j -= 1  # j指针后移  
        else:  
            i += 1  # i指针后移  
  
    return lst  
  
# 测试样例  
print(move_zeros_to_end) 
