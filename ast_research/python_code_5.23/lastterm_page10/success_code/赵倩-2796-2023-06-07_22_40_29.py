a=list(input())
b=[]
c=[]
l=0
long=len(a)
while 1:
    if l==long-1:
        if a[l].isdigit():
            b.append(a[l])
            c.append(b)
            b=[]
        break
    elif a[l].isdigit() and a[l+1].isdigit():
        b.append(a[l])
    elif a[l].isdigit() and a[l+1].isdigit()!=True:
        b.append(a[l])
        c.append(b)
        b=[]
    l+=1
l=0
for i in c:
    if len(i)>l:
        l=len(i)
lst1=[]
for i in c:
    if len(i)==l:
        lst1=i
if len(lst1)!=0:
    for i in lst1:
        print(i,end="")
else:
    print("No digits")





    



        

       



                    




