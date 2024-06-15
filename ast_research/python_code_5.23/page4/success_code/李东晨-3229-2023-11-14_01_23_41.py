n=eval(input())
b=[]
k=False
for x in n:
    if n.count(x)==1:
       k=True
       b.append(x)
       b.sort()
       m=",".join(map(str,b))
print(m) 
if k==False:
    print("False")

