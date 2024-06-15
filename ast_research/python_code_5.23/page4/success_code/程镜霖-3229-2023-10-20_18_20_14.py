lst=eval(input())
lst.sort()
x=[]
for i in lst:
    if lst.count(i)==1:
       x.append(i)
    else:
        pass
if x==[]:
    print("False")
else:
    x=int(",".join(x))
print(x)



