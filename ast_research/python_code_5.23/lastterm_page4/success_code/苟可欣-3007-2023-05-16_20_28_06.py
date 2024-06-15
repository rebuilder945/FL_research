ls=eval(input())
n,m=eval(input())
if m>len(ls)-1 or n>len(ls)-1:
    print("error")
else:
    ls1=ls[:n+1]
    ls2=ls[m:]
    ls1.extend(ls2)
    print(ls1)
