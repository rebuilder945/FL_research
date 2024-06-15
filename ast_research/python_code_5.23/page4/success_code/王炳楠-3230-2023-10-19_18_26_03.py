ls=eval(input())
ls.sort(reverse=True)
c=""
for i in ls[::1]:
    c=c+"%d"%(i)
print(eval(c))


