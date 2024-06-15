n=eval(input())
b=[]
k=False
for x in n:
    if n.count(x)==1:
       k=True
       b.append(x)
       b.sort()
       m=",".join(map(str,b))
else: 
    if k==False:
        print("False")
if b==[]:
    print("False")
else:
    print(m)

