a=input()
b=input()
c=len(b)
d=''
for i in range(len(a)):
    if a[i,i+c]!=b:
        d+=a[i,i+c]
print(d)
