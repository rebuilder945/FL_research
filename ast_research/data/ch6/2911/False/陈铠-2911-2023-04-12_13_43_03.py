x=list(input())
lst=[]
for i in x:
    a=(int(i)+5)%10
    lst.append(a)
lst[0],lst[-1]=lst[-1],lst[0]
lst[1],lst[-2]=lst[-2],lst[1]
print("".join(str(c) for c in lst))
