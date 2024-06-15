a=list(input().split(','))
b=eval(input())
x=[]
for i in range(len(a)):
    s=[]
    s.append(a[i])
    s.append(b[i])
    x.append(s)
print(x)    
