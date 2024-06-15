lst=eval(input())
lst.sorted(reverse=True)
sum=""
for x in lst:
    sum+=str(x)
print(int(sum))
