# 输入列表  
lst = list(map(int, input().split(',')))  
  
# 输入n和m  
n, m = map(int, input().split(','))  
  
# 检查n和m是否在列表范围内  
if n >= 0 and n < len(lst) and m >= 0 and m < len(lst):  
    # 删除n~m之间的元素，不包括m位置的元素  
    lst = lst[:n] + lst[n+1:m] + lst[m+1:]  
else:  
    print("error")  
  
# 输出处理后的列表  
print(lst)
