list=eval(input())
list.reverse()
a=[]
for x in list:
    if x not in a:
        a.append(x)
a.reverse()
print(a)
