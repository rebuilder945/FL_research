ls=eval(input())
ls.sort(reverse=True)
max=''
for i in range(len(ls)):
    max+=str(ls[i])
print(int(max))

