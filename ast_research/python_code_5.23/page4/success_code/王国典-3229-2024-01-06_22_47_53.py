ls=eval(input())
kong=[]
for x in ls:
    a=ls.count(x)
    if a==1:
        kong.append(x)
if kong==[]:
    print("False")
if kong!=[]:
    strls=[str(y) for y in kong]
    zhengli=sorted(strls,reverse=False)
result=",".join(zhengli)
print(result)



