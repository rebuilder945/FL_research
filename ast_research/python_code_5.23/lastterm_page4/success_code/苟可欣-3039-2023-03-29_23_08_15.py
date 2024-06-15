ls=eval(input())
a=[]
for x in ls:
    if x==max(ls) or x==min(ls):
        continue
    else:
        a.append(x)
print(a)
