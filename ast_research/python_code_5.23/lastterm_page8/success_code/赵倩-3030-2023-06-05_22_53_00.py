a=input().split(",")
b=input().split(",")
list=[]
c=len(a)
while len(a)!=0:
    list.append([a[0],int(b[0])])
    del a[0]
    del b[0]
l=[]
s=[]
for i in list:
    l.append(i[::-1])
l=sorted(l)
for i in l:
    s.append(i[::-1])
print(s)

    

        

       



                    




