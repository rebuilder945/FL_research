lst = eval(input())
m = sum(lst)/len(lst)
if sum(lst)%len(lst)==0:#"%"为取余运算，0表示小数结果
    print('%d'%m)#“%d”表示十进制整数
else:
    print('%.2f'%m)
