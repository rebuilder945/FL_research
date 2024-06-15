s=eval(input())
ls=[]
for i in s:
    if s.count(i)==1:
        i=str(i)
        ls.append(i)
ls.sort()
if len(ls)==0:
    print("False")
else:
    x=",".join(ls)
    print(x)        
