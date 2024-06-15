n=eval(input())
b=[]
for x in n:
    if n.count(x)==1:
       b.append(x)
       b.sort()
       m=",".join(map(str,b))
    elif b==[]:
        print("False")
print(m) 
