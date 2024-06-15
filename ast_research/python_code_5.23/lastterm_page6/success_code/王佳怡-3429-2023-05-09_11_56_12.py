s=input()
a=0
b=0
c=0
d=0
for x in s:
    if x.isalpha():
        a=a+1
    if x.isdigit():
        c=c+1
    if x==" ":
        b=b+1
d=len(s)-a-b-c
print(a,b,c,d)
