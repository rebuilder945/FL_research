# a=eval(input())
# b=sum(a)
# c=b/(len(a))
# if c%1==0:
#     print("%d"%c)
# else:
#     print('%.2f'%c)
# a=eval(input())
# b=[max(a),min(a)]
# c=a.copy()
# for i in c:
#     if i in b:
#         a.remove(i)
# print(a)
# ls = eval(input())
# ls2 = []
# for i in range(len(ls)):
#     if ls[i:].count(ls[i]) == 1:
#         ls2.append(ls[i])
# print(ls2)
# n=input()
# a=[x+1 for x in range(int(n))]
# a.remove(1)
# a.append(1)
# print(a)
# a
a=list(map(int,input().split(',')))
n,m=eval(input())
if n>len(a)-1 or m>len(a)-1:
    print("error")
else:
    c=a[n]
    for i in range(m):
        a.append(c)
    print(a)







