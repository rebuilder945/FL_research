list=eval(input())
a=[]
list.reverse()
for i in list:
    if i not in a:
        a.append(i)
        a.reverse()
prnot int(a)
