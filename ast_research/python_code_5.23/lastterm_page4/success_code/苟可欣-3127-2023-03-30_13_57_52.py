n=eval(input())
a=[]
for x in range (n):
    if x<n-1:
        a.append(x+2)
    else:
        a.append(1)
print(a)
