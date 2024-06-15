'''【问题描述】从键盘输入两个整数n和m（要求n<m），编程求出由n到m(不包含m)中的整数组合而成的所有不含重复数字的三位数。
若n和m的输入不合法或者没有符合条件的三位数则提示输出“illegal input"。

【输入形式】输入一行，内容为两个以空格分隔的整数，分别表示n和m。

【输出形式】以空格分隔输出所有符合条件的三位数。'''
list1=list(input().split(" "))
n=eval(list1[0])
m=eval(list1[1])
b=[]
if n%1!=0 or m%1!=0 or n>=m or m-n<3:
    print("illegal input")
else:
    for i in range(0,m-n):
        a=list(range(n,m))
        I=a[i]
        del a[i]
        for j in range(len(a)):
            a=list(range(n,m))
            del a[i]
            J=a[j]
            del a[j]
            for k in range(len(a)):
                K=a[k]
                b.append((str(I)+str(J)+str(K)))
    print(*b,sep=' ')
