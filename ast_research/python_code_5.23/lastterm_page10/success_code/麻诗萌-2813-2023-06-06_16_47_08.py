a=input().split()
b=input()
for i in a:
    if i==b:
        a.remove(b)
print("".join(a))
