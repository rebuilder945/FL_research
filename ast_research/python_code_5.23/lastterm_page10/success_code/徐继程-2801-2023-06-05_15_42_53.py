string=input()
star=0
for x in range(len(string)):
    if ord(string[x])<=ord('9') and ord(string[x])>=ord('0'):
        star+=1
        break
for x in range(len(string)):
    if ord(string[x])<=ord('z') and ord(string[x])>=ord('a'):
        star+=1
        break
for x in range(len(string)):
    if ord(string[x])<=ord('Z') and ord(string[x])>=ord('A'):
        star+=1
        break
for x in range(len(string)):
    if string[x] in ['~','!','@','#','$','%','^','&','*','()','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\']:       
        star+=1
        break
if len(string)>=8:
    star+=1
print(star)
