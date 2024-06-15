l=eval(input())
l.reverse()
a=[]
for i in l:
    if i not in a:
        a.insert(0,i)
print(a)
