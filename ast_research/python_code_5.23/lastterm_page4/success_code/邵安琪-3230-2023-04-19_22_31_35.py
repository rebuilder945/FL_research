lst=eval(input())
lst.sort(reverse=True)
sum=""
for x in lst:
    sum+=str(x)
print(int(sum))
