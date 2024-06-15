s = input()
a = 0
b=0
c=0
d=0
for i in s:
    if i.isalpha():
        a+=1
    if i.isdigit():
        b+=1
    if i==" ":
        c=c+1
d = len(s)-a-b-c
print(a,c,b,d)
