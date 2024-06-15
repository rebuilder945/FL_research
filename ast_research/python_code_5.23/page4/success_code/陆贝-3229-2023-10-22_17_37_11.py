lt=eval(input())
ii=list()
ls=[]
for i in lt:
    a=lt.count(i)
    if a==1:
            ls.append(i)
print(ls)
if ls==[]:
    print("False")
else:
     l=len(ls)
     for i in range(l):
          a=min(ls)
          ii.append(a)
          ls.remove(a)
          
