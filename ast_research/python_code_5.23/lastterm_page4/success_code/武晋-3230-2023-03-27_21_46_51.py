b=eval(input())
b.sort()
sum=''
for i in range(len(b)):
    sum+=str(b[i])
print(int(sum))
