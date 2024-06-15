a = input()
lst1 = "\~!@#$%^&*()_=-/,.?<>;:[]{}|"
lst2 = "1234567890"
s = 0
for i in a:
    if i in lst1:
        s+=1
        break
for i in a:
    if i in lst2:
        s+=1
        break
for i in a:
    if i.islower():
        s+=1
        break
for i in a:
    if i.isupper():
        s+=1
        break
if len(a) >= 8:
    s+=1
print(s)
