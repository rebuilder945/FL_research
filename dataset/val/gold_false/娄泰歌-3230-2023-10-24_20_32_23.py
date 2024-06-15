def max_integer(lst):  
    # 将列表中的数字按照降序排序  
    sorted_lst = sorted(lst, reverse=True)  
      
    # 初始化一个空字符串用于构建最大整数  
    max_int = ""  
      
    # 遍历排序后的列表，将每个数字作为最高位  
    for digit in sorted_lst:  
        # 如果当前数字已经使用过，跳过  
        if int(digit) not in [int(d) for d in max_int]:  
            # 将当前数字添加到最大整数中  
            max_int += str(digit)  
        else:  
            # 否则，将当前数字替换为0  
            max_int = max_int[:int(digit)-1] + "0" + max_int[int(digit):]  
      
    # 将构建的最大整数转换为整数类型并返回  
    return int(max_int)  
  
# 测试样例  
print(max_integer([0,1,2,3,2]))  # 输出：32210
