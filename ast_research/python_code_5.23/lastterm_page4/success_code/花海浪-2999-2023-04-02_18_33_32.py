# a=eval(input())
# b=sum(a)
# c=b/(len(a))
# if type(c)==float:
#     print('%.2f'%c)
# else:
#     print(int(c))
ls = input().split()
n,m = map(int,input().split())
# print(n,m)
ls[n],ls[m] = ls[m],ls[n]
print(ls)
