lst=eval(input())
lst.sort()
n=[]
for i in lst:
    if lst.count(i)==1:
        n.append(i)
    else:
        continue
if n==[]:
    print("False")
else:
    print(n)
