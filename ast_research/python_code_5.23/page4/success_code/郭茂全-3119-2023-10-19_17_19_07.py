list=eval(input())
a=[]
for x in list:
    if x not in a:
        a.append(x)
print(a)
