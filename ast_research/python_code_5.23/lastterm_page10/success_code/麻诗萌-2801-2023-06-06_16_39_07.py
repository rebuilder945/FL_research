n=input()
s=0
m="~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
x=list(m)
if len(n)>=8:
    s=s+1
for i in n:
    if i.isdigit():
        s+=1
        break
for i in n:
    if i.islower():
        s+=1
        break
for i in n:
    if i.isupper():
        s+=1
        break
for i in n:
    if i in m:
        s+=1
        break
print(s)

