a=eval(input())
a.sort(reverse=True)
x=''    
i=0
while i<len(a):
    x=x+str(a[i])
    i=i+1
x=int(x)    
print(x)


