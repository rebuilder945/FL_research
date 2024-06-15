ls=eval(input())
lst=[]
for i in ls:
    if ls.count(i)==1:
        lst.append(str(i))
lst.sort()
if lst==[]:
    print("False")
else:
    print(",".join(lst))



