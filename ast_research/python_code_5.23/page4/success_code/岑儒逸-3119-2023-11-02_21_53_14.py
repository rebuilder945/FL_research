ls=eval(input())
ls1=[]
a=len(ls)
m=0
while m<a:
    for x in ls:
        if ls.count(x)>1:
            ls.remove(x)
    m+=1
print(ls)
