a=eval(input())
b=max(a)
c=min(a)
for x in range(len(a)):
    if x==b or x==c:
        a.remove(x)
print(a)
