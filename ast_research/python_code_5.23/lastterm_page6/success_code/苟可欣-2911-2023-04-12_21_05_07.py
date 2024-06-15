a=eval(input())
lst=[]
d=0
while a>0:
    b=(a%10+5)%10
    lst.append(b)
    a=a//10
for x in range(int(len(lst)/2-1)):
    lst[x],lst[-(x+1)]=lst[-(x+1)],lst[x]
for c in lst:
    d=d*10+c
print(d)

