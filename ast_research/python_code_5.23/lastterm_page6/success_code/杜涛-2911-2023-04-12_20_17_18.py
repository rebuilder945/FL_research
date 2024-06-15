num=input()
lst=list(num)
for i in range(len(lst)):
    lst[i]=(eval(lst[i])+5)%10
a,b,c,d=lst[0],lst[1],lst[-1],lst[-2]
lst[0]=str(c)
lst[-1]=str(a)
lst[1]=str(d)
lst[-2]=str(b)
print("".join(lst))





