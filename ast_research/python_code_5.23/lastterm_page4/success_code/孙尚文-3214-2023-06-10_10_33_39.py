a=eval(input())
b=[]
for i  in a:
    if i==0:
        a.remove(i)
        a.append(i)

print(a)
