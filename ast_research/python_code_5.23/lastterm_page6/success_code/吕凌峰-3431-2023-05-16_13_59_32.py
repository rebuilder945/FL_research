# 轮盘赌的颜色
# 【问题描述】
# 在一个赌博用的转盘上，口袋的编号是从0到36，口袋的颜色如下： 
# 从1号袋到10号袋，奇数的口袋是红色，偶数的口袋是黑色。
# 从11号袋到18号袋，奇数的口袋是黑色，偶数的口袋是红色。
# 从19号袋到28号袋，奇数的口袋是红色，偶数的口袋是黑色。 
# 从29号袋到36号袋，奇数的口袋是黑色，偶数的口袋是红色。
# 0号口袋是绿色
# 请编写一个程序，根据用户输入的口袋编号，输出口袋的颜色。
# 如果用户输入的数字不在0~36这个范围内，则输出“error”。

n = eval(input())
if n % 2 ==0:
    flag = True
else:
    flag = False
if n == 0:
    print('green')
elif n >= 1 and n <= 10:
    if flag == True:
        print('black')
    else:
        print('red')
elif n >= 11 and n <= 18:
    if flag == False:
        print('black')
    else:
        print('red')
elif n >= 19 and n <= 28:
    if flag == True:
        print('black')
    else:
        print('red')
elif n >= 29 and n <= 36:
    if flag == False:
        print('black')
    else:
        print('red')
else:
    print('error')
