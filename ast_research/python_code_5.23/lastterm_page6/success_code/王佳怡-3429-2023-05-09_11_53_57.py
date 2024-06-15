s=input()
a=0
b=0
c=0
d=0
for x in s:
    if x.isalpha():
        a=a+1
    if x.isdigit():
        b=b+1
    if x==" ":
        c=c+1
    else:
        d=d+1
print(a,b,c,d)
