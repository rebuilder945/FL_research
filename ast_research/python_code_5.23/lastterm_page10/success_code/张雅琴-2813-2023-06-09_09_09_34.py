a=input()
b=input()
if b not in a:
    print(a)
else:
    for i in a:
        if i==b:
            a=a.replace(i,'')
print(a)
