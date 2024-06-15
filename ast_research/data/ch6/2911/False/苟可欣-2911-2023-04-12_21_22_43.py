a=eval(input())
lst=[]
d=""
while a>0:
    b=(a%10+5)%10
    lst.append(b)
    a=a//10
for x in range(int(len(lst)/2)-2):
    lst[x],lst[-(x+1)]=lst[-(x+1)],lst[x]
for x in lst:
    d="%s"%(x)+"%s"%(d)
print(d)

