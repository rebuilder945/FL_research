lt=eval(input())
ii=list()
ls=[]
for i in lt:
    a=lt.count(i)
    if a==1:
            ls.append(i)
if ls==[]:
    print("False")
else:
     ls.sort()
     z=""
     for i in ls:
          x=str(i)
          z=z+x
     z=",".join(z)
     print(z)

