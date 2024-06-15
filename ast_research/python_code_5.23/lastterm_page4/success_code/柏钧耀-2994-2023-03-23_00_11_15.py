lst=eval(input())
n,m=eval(input())
lst=list(lst)
if n>len(lst)>0:
    print("error")
elif n<len(lst)<0:
    print("error")
else:
    ls2=[]
    for i in range(m):
        ls2.append(lst[n])
    ls3=lst+ls2
    print(ls3)

