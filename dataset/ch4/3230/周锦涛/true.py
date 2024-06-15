ls=eval(input())
ls.sort(reverse=True)
m=''
for i in range(len(ls)):
    x=str(ls[i])
    m=m+x
print(int(m))
