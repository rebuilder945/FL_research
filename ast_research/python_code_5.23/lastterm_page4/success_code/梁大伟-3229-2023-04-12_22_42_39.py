lst=eval(input())
ls=[]
for i in lst:
    if lst.count(i)==1 and i not in ls:
        ls.append(i)
if ls==[]:
    print(False)
ls.sort()
a=""
a=",".join(map(str,ls))
print(a)
