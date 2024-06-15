s=input()
a=0
s1="'~','!','@','#','$','%','^','&','*','()','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\'"
for i in s:
    if i.isdigit():
        a+=1
        break
for i in s:
    if i.isalpha()and i==i.lower():
        a+=1
        break
for i in s:
    if i.isalpha()and i==i.upper():
        a+=1
        break
for i in s:
    if i in s1:
        a+=1
        break
if len(s)>=8:
    a+=1
print(a)
