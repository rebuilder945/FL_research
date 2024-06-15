num=input()
u=""
c=0
for i in num:
    if i.isdigit():
        u=u+i
        c+=1
    else:
        u=u+" "
if c==0:
    print("No digits")
else:    
    lst=list(u.split(" "))
    lst.sort(reverse=False)
    print(lst[-1])
