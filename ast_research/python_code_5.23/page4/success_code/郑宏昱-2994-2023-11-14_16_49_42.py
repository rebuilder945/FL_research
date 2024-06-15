# 输入列表元素  
input_str = input()  
input_list = [item for item in input_str.split(',') if item != '']  
  
# 输入n和m  
n_str, m_str = input().split(',')  
n = int(n_str)  
m = int(m_str)  
  
# 检查n是否在列表下标范围内  
if n >= len(input_list):  
    print("error")  
else:  
    # 将第n个元素重复m次，添加到列表末尾  
    input_list.extend([input_list[n]] * m)  
    input_list = list(map(int,input_list))
    print(input_list)

