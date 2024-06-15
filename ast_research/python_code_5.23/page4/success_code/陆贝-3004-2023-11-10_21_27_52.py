def susu(n):
    for i in range(2,n-1):
        if n%i==0:
            break
    else:
        return True
t=[]
a=eval(input())
for i in a:
    if susu(i):
        t.append(i)
print(i)




