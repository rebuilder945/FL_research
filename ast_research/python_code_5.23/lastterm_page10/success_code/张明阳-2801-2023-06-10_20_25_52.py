a=input()
lst1="\~!@#$%^&*()_=-/,.?<>;:[]}{|"
lst2="1234567890"
jishu=0
for i in a:
    if i in lst2:
        jishu+=1
        break
for i in a:
    if i.islower():
        jishu+=1
        break
for i in a:
    if i.isupper():
        jishu+=1
        break
if len(a)>=8:
    jishu+=1
for i in a:
    if i in lst1:
        jishu+=1
        break
print(jishu)







