s=input()
xingji=0
panbie="~!@#$%^&*()_=-/,.<>;:[]|"+"{"+"}"
for i in s:
    if i.isdigit() is True:
        xingji+=1
        break
for i in s:
    if i.islower() is True:
        xingji+=1
        break
for i in s:
    if i.isupper() is True:
        xingji+=1
        break
if len(s)>=8:
    xingji+=1
a=set(panbie)
b=set(s)
if len(a&b)>0:
    xingji+=1
print(xingji)

