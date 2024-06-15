l = eval(input())
lf =[]
for i in l:
    if l.count(i)<=1:
        lf.append(i)
print(lf)
