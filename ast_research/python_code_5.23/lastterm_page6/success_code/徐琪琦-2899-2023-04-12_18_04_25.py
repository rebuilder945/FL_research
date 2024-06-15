#从键盘输入两个整数n和m (要求n<m),求出由n到m(不包含m)中的整数组合而成的所有不含重复数字的三位数,若n和m的输入不合法或者没有符合条件的三位数则提示输出“illegal input"。
n,m = map(int,input().split())
if n >= m or n - m < 3 :
    print("illegal input")
else:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and a != c and b != c and a != 0:
                    print(100*a+10*b+c,end = " ")










# n,m = map(int,input().split())
# for a in range(n,m):
#     for b in range(n,m):
#         for c in range(n,m):
#             if a != b and b != c and c != a:
#                 N = a *100 + b *10 + c
#                 if N > 99:                    #为了避免0打头的情况
#                     print(N,end = "")
# else:
#     print("illegal input")



