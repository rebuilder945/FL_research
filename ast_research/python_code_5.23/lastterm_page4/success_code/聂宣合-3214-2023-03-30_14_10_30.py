lst=eval(input())
out=[]
others=[]
for i in lst:
    if i == 0:
        out.append(i)
    else:
        others.append(i)
sums=others+out
print(sums)
