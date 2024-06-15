a=eval(input())
b=max(a)
c=min(a)
for i in range(len(a)-1,-1,-1):
    if a[i]==b:
          a.pop(a[i])
    elif a[i]==c:
          a.remove(c)
print(a)



