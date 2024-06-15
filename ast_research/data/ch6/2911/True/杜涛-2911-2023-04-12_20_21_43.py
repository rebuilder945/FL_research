num=input()
lst=list(num)
for i in range(len(lst)):
    lst[i]=(eval(lst[i])+5)%10
a,b,c,d=lst[0],lst[1],lst[-1],lst[-2]
lst[0]=c
lst[-1]=a
lst[1]=d
lst[-2]=b
for i in range(len(lst)):
    lst[i]=str(lst[i])
print("".join(lst))





