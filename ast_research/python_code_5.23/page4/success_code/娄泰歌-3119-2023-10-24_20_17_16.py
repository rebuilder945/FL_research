def remove_duplicates(lst):  
    return list(dict.fromkeys(lst))  
  
# 输入列表  
lst = [4,3,2,3,2,4,True]  
  
# 删除重复元素  
lst = remove_duplicates(lst)  
  
# 输出列表  
print(lst)
