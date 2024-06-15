
s=list(input())
a=0
c="\~!@#$%^&*()_=-/,.?<>;:[]}{|"
for i in range(len(s)):
    if s[i].isdigit():
        a+=1
        break
for i in range(len(s)):
    if s[i].islower():
        a+=1
        break
for i in range(len(s)):
    if s[i].isupper():
        a+=1
        break

if len(s)>=8:
    a+=1
for i in range(len(s)):
    if s[i] in c:
        a+=1
        break
print(a)



