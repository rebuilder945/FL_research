l=list(input())
s=0
t="\~!@#$%^&*()_=-/,.?<>;:[]}{|"
l2=list(t)
for i in l:
    if len(l)>=8:
        s+=1
        break
for i in l:
    if i.isnumeric():
        s+=1
        break
for i in l:
    if i.islower():
        s+=1
        break
for i in l:
    if i.isupper():
        s+=1
        break
for i in l:
    if i in t:
        s+=1
        break
print(s)
