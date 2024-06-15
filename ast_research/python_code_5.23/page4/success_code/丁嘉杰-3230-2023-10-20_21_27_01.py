ls1=eval(input())
ls1.sort(reverse=True)
sum=''
for i in range(len(ls1)):
    sum+=str(ls1[i])
print(int(sum))
