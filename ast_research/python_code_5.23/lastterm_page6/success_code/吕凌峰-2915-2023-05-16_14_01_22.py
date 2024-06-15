# python水仙花数
# 【问题描述】输入一个整数，输出小于等于该整数的所有水仙花数
# 每行输出一个，若没有水仙花数则输出“none”
# “3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身
# 例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC

def shuixianhuashu(x):
    Sum = 0
    for i in str(x):
        a = int(i)
        Sum += a ** 3
    if Sum == x and x != 0 and x != 1:
        return True
    else:
        return False


num = eval(input())
nums = [x for x in range(num + 1)]
Output = []
for i in nums:
    if shuixianhuashu(i):
        Output.append(i)
    else:
        pass
if Output == []:
    print("none")
else:
    for i in Output:
        print(i)
