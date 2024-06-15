lst=eval(input())
lst.sort(reverse=True)
total=""
for x in lst:
    total+=str(x)
print(total)

