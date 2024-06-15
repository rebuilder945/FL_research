ls=eval(input())
a=max(ls) 
b=min(ls)
newls=[]
for i in ls:
    if i!=a and i!=b:
        newls.append(i)
print(newls)
