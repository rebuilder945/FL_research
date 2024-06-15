mima=0
m=input()
lst1="\~!@#$%^&*()_=-/,.?<>;:[]}{|"
lst2="1234567890"
for i in m:
    if i in lst1:
        mima+=1
        break
for i in m:
    if i.isupper():
        mima+=1
        break
for i in m:
    if i.islower():
        mima+=1
        break
for i in m:
    if i in lst2:
        mima+=1
        break
if len(m)>=8:
    mima+=1
print(mima)

