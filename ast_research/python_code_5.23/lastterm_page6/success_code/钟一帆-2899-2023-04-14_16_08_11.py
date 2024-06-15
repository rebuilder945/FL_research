#【问题描述】从键盘输入两个整数n和m（要求n<m），
#编程求出由n到m(不包含m)中的整数组合而成的所有不含重复数字的三位数。
#若n和m的输入不合法或者没有符合条件的三位数则提示输出“illegal input"。
#【输入形式】输入一行，内容为两个以空格分隔的整数，分别表示n和m。
#【输出形式】以空格分隔输出所有符合条件的三位数。
n,m=map(int,input().split(' '))
if 0<=n<m<=10 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    N=a*100+b*10+c
                    if N>99:
                        print(N,end=' ')
else:print('illegal input')




