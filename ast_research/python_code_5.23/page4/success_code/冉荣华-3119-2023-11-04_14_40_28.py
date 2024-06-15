x=eval(input())
x.reverse
a=[]
for i in x:
    if i not in a:
        a.append(i)
a.reverse
print(a)
