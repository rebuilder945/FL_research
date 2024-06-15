a=list(input())
b=input()
for x in a:
    if x==b:
        a.remove(x)
print("".join(a))
