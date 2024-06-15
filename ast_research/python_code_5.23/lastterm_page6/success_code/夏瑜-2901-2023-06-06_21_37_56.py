a=input()
list=[]
i=1
while i>=0:
    if a=="#":
        break
    else:
        list.append(int(a))
        i+=1
        a=input()
m=len(list)
n=sum(list)
print("%d %d"%(m,n))


