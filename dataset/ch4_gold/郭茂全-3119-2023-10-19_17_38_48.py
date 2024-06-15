list=eval(input())
a=[]
for x in list[-1::-1]:
    if x not in a:
        a.append(x)
a.reverse()
print(a)
