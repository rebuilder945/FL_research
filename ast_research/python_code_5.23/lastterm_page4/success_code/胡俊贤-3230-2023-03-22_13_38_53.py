ls=eval(input())
ls.sort(reverse=True)
new=[]
for i in ls:
    j=str(i)
    new.append(j)
print(''.join(new))

