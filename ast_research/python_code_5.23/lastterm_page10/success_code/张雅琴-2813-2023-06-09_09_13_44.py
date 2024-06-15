a=input()
b=input()
if b not in a:
    print(a)
else:
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[i:i+j+1]==b:
                a=a.replace(a[i:i+j+1],'')
print(a)
