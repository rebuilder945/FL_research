ls=eval(input())
ls.sort(reverse=True)
sum=""
for i in range(len(ls)):
    sum+=str(ls[i])
print(int(sum))
