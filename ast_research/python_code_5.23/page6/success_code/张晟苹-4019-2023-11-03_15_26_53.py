def qwq(n):
    lst1=[]
    if n:
        lst1=qwq(n//10)
        return lst1+list(str(n%10))
n=eval(input())
lst2=[]
flag=False
for i in range(len(str(n))):
    if n:
        b1=n%10
        b2=(b1+5)%10
        lst2.append(b2)
        flag=True
    n=n//10
ls3=list(map(str,lst2))
print(ls3[0]+ls3[1]+ls3[2])

