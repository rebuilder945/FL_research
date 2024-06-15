ls=eval(input())
ls.reverse()
ls1=[]
for i in ls:
    if i not in ls1:
        ls1.insert(0,i)
print(ls1)
