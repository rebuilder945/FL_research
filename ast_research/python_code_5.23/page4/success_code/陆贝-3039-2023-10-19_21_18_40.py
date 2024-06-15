lt=eval(input())
a=max(lt)
b=min(lt)
ls=[]
for i in it:
    if i!=a and i!=b:
        ls.append(i)
print(ls)
