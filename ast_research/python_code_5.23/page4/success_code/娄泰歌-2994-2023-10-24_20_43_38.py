def move_element(lst, n, m):  
    # 检查n是否超出列表范围  
    if n < 0 or n > len(lst):  
        return "error"  
      
    # 把第n个元素重复m次，放到列表尾部  
    lst.extend([lst[n]] * m)  
      
    return lst  
  
# 读取用户输入  
input_str = input()  
# 用逗号分隔输入，得到列表元素  
lst = list(input_str.split())  
  
# 读取n和m的值  
n, m = map(int, input().split())  
  
# 调用函数并打印结果  
print(move_element(lst, n-1, m))  # 注意：Python的列表索引从0开始，因此需要将n减1
