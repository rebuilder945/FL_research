n=eval(input())
a=[]
n.reverse()
for i in n:
    if i not in a:
        a.append(i)

a.reverse()
print(a)






