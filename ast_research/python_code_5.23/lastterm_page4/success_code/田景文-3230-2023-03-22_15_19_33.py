a=eval(input())
b=a.sort(reverse=True)
sum=''
for i in range(len(a)):
    sum+=str(a[i])
print(int(sum))
