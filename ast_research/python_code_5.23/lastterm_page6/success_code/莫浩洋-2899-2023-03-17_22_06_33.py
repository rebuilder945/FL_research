'''【问题描述】从键盘输入两个整数n和m（要求n<m），编程求出由n到m(不包含m)中的整数组合而成的所有不含重复数字的三位数。
若n和m的输入不合法或者没有符合条件的三位数则提示输出“illegal input"。

【输入形式】输入一行，内容为两个以空格分隔的整数，分别表示n和m。

【输出形式】以空格分隔输出所有符合条件的三位数。'''
list1=list(input().split(" "))
n=list1[0]
m=list1[1]
b=[]
if type(n)!=int or type(m)!=int or n>=m:
    print("illegal input")
else:
    for i in range(0,m-n):
        a=list(range(n,m))
        del a[i]
        for j in range(len(a)):
            a=list(range(n,m))
            del a[i]
            del a[j]
            for k in range(len(a)):
                a=list(range(n,m))
                del a[i]
                del a[j]
                b.append((str(i)+str(j)+str(k)))
    print(*b,sep=' ')
