a=input().split(sep=",")
b=input().split(sep=",")
n=eval(b[0])
m=eval(b[-1])
c=len(a)
lt=[]
for i in a:
    i=eval(i)
    lt.append(i)
if n>c-1 or n<-c:
    print("error")
else:
    t=lt[n]
    z=t*m
    lt=lt+z
    print(lt)
