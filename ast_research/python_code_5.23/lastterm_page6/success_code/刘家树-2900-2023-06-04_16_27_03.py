n=eval(input())
if n<0 or n==float:
    print("illegal input")
def f(x):
    for i in range(2,x//2+1):
         if x%i==0:
             break
         else:
             return x
a=[]
for x in range(n+1):
    if f(x)==x and f(str(x)[::-1])==str(x)[::-1]:
        a.append(x)
    else:
        pass
for x in a:
    print(x,end=" ")













