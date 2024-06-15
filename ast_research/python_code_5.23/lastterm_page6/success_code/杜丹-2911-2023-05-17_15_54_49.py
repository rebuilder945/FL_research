num = input("请输入要加密的数字：")
new_num = []
for i, n in enumerate(num): 
    new_n = (int(n) + 5) % 10    
    new_num.append(str(new_n))# 将第一位和最后一位交换，第二位与倒数第二位交换
for i in range(len(new_num) // 2):    
    new_num[i], new_num[-i-1] = new_num[-i-1], new_num[i]# 输出加密后的数字密码
print("加密后的密码为：", ''.join(new_num))

