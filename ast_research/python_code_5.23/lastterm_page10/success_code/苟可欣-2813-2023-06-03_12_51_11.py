a=input()
b=input()

for x in range(len(a)):
    if a[x]==b[0]:
        if a[x:x+len(b)]==b:
            del a[x:x+len(b)]
print(a)
