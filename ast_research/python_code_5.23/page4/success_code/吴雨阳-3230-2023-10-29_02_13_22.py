ls=eval(input())
ls.sort()
ls.reverse()
sum=""
for i in range(len(ls)):
    sum+=str(ls[i])
print(int(sum))
