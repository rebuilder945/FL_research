a=input()
lst=list(a)
star=0
lst1="\~!@#$%^&*()_=-/,.?<>;:[]}{|"
lst2="1234567890"
for i in lst:
    if i in lst2:
        star+=1
        break
for i in lst:
    if i.islower():
        star+=1
        break
for i in lst:
    if i.isupper():
        star+=1
        break
if len(lst)>=8:
    star+=1
for i in lst:
    if i in lst1:
        star+=1
        break
print(star)
