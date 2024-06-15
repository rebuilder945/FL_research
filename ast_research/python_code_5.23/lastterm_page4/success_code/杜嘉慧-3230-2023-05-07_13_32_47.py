lst=eval(input())
lst.sort(reverse=True)
a=0
for x in lst:
    a=a*10+x
print(a)

