a=eval(input())
a.reverse()
ls1=[]
for i in a:
    if i not in ls1:
        ls1.insert(0,i)
print(ls1)
