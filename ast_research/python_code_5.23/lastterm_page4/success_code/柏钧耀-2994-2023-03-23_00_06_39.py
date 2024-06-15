lst=input().split(',')
n,m=eval(input())
if n>len(lst)>0:
    print("error")
elif n<len(lst)<0:
    print("error")
else:
    a=lst[n]
    ls2=[]
    for i in range(m):
        ls2.append(a)
    ls3=lst+ls2
    print(ls3)

