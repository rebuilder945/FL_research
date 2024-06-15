lines = input().split()  # 输入字符串列表  
n, m = map(int, input().split())  # 输入两个整数n和m  
  
lines[n], lines[m] = lines[m], lines[n]  # 交换元素  
  
print(lines)  # 输出交换后的列表
