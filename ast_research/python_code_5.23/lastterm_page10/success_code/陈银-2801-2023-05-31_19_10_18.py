code = input()
star = 0
level1=[]
level2=[]
level3=[]
level4=[]
if len(code)>=8:
    star += 1
for x in code:
    if 47<=ord(x)<=57:
        level1.append(x)
    elif 97<=ord(x)<=122:
        level2.append(x)
    elif 65<=ord(x)<=90:
        level3.append(x)
    elif x in "~!@#$%^&*()_=-/,.?<>;:[]{}|\ ":
        level4.append(x)
list = [level1,level2,level3,level4]
print(list)
for y in list:
    if y !=[]:
        star += 1
print(star)
