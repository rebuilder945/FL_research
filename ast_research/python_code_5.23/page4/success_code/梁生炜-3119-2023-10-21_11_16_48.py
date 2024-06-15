ls=eval(input())
ls1=[]
ls.reverse()
for i in ls:
    if i not in ls1:
        ls1.insert(0,i)
print(ls1)
