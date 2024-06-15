a=input()
k=0
for x in a:
    if x.isdigit():
        k=k+1
        break
for x in a:
    if x.isupper():
        k=k+1
        break
for x in a:
    if x.islower():
        k=k+1
        break
if len(a)>=8:
    k=k+1
f="~!@#$%^&*()_=-/,.?<>;:[]{}|"
for x in a:
    if x in f:
        k=k+1
print(k)
