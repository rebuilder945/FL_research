dic={}
ls1=[]
ls2=[]
while  True:
        a=str(input())
        if a=="ok":
            break
        if a!="ok":
            ls1.append(str(a[0:-3]))
            ls2.append(int(a[-2:]))
ls1.sort()
print(ls1)
for i in ls2:
    ls2[ls2.index(i)]=int(i)
ls2.sort()
print(ls2)
if "India" not in ls1:
    print("no")
else:
    print("yes")
c=sum(ls2)
print(int(c))



