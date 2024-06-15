ls=eval(input())
x=max(ls)
y=min(ls)
ls2=[i for i in ls if i not in [x,y]]
print(ls2)
