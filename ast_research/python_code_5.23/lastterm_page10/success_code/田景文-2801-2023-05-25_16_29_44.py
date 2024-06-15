s = input()
x = 0
s1 = []
s2 = []
s3 = []
s4 = []
for i in s:
    if i.isdigit():
        s1.append(i)
    if i.isupper():
        s2.append(i)
    if i.islower():
        s3.append(i)
    if i in ('~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\'):
        s4.append(i)
if s1 != []:
    x += 1
if s2 != []:
    x += 1
if s3 != []:
    x += 1
if s4 != []:
    x += 1
if len(s) >= 8:
    x += 1
print(x)
