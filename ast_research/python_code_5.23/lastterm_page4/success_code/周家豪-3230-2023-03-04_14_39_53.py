lst1=eval(input())
lst1.sort(reverse=True)
sum=""
for i in lst1:
    sum+=str(i)
print(int(sum))

