list=input()
a=[]
list.reverse()
for i in list:
    if i not in a:
        a.append(i)
    else:
        break
print(a)
