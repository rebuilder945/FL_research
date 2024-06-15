s=eval(input())
s.reverse()
ls=[]
for i in s:
    if i not in ls:
        ls.insert(0,i)
print(ls)
