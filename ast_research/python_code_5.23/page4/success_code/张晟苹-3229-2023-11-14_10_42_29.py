a=eval(input())
ls=[]
for i in a:
    if a.count(i)==1:
        ls.append(i)
        b=ls.sort()
    if ls==[]:
        b='False'
    else:
        b=','.join(list(map(str,ls)))
print(b)
        

