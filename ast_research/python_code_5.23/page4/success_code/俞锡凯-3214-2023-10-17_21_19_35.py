a=eval(input())
b=[]
for i in a:
    if i==0:
        c=a.count(0)
        a.remove(i)
for i in range(c):
    a.append(0)
print(a)

        
