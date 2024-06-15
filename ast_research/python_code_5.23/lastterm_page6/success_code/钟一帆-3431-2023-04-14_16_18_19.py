#在一个赌博用的转盘上，口袋的编号是从0到36，口袋的颜色如下： 
#从1号袋到10号袋，奇数的口袋是红色，偶数的口袋是黑色。
#从11号袋到18号袋，奇数的口袋是黑色，偶数的口袋是红色。
#从19号袋到28号袋，奇数的口袋是红色，偶数的口袋是黑色。 
#从29号袋到36号袋，奇数的口袋是黑色，偶数的口袋是红色。
#0号口袋是绿色
#请编写一个程序，根据用户输入的口袋编号，输出口袋的颜色。
# 如果用户输入的数字不在0~36这个范围内，则输出“error”。
n=int(input())
if 1<=n<=10 and n%2==0:
    print('black')
elif 1<=n<=10 and n%2!=0:
    print('red')
elif 11<=n<=18 and n%2==0:
    print('red')
elif 11<=n<=18 and n%2!=0:
    print('black')
elif 19<=n<=28 and n%2==0:
    print('black')
elif 19<=n<=28 and n%2!=0:
    print('red')
elif 29<=n<=36 and n%2==0:
    print('red')
elif 29<=n<=36 and n%2!=0:
    print('black')
elif n==0:
    print('green')
else:
    print('error')    
