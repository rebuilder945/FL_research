str1=list(x for x in input())
str2=['~','!','@','#','$','%','^','%','*','()','-','_','+','=',':',';',',','[',']','{','}']
star=0
if len(str1)>=8:
    star+=1
for x in str1:
    if type(eval(x))==int:
        star=+1
        break
for x in str1:
    if ord('a')<=ord(x)<=ord('z'):
        star+=1
        break
for x in str1:
    if x in str2:
        star+=1
        break
for x in str1:
    if x in str2:
        star+=1
        break
print(star)


