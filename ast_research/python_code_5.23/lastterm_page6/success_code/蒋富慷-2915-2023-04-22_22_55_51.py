#【问题描述】
#输入一个整数，输出小于等于该整数的所有水仙花数，每行输出一个，若没有水仙花数则输出“none”
#“3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身。例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。 
#【输入形式】 
#【输出形式】 
#【样例输入】
     #100

def flower(number):
    a = number
    temp = 0
    while number != 0:
        temp += (number % 10) ** 3
        number = number // 10
    if a == temp:
        print(a)
        return True

flag = 0
number = int(input())
for i in range(2,number+1):
    if flower(i):
        flag = 1
if flag == 0:
    print('none')


