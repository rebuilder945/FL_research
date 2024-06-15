n=str(input())
c="~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
b="0123456789"
a=0
if len(n)>=8:
    a=1
for i in range(len(n)):
    if n[i] in b:
        a=a+1
        break
for i in range(len(n)):
    if n[i].islower():
        a=a+1
        break
for i in range(len(n)):
    if n[i].isupper():
        a=a+1
        break
for i in range(len(n)):
    if n[i] in c:
        a=a+1
        break
print(a)                    
