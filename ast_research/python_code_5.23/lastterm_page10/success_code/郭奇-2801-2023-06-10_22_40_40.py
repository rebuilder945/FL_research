a=input()
strength=0
if a.isupper():
    strength+=1
if a.islower():
    strength+=1
if a.isdigit():
    strength+=1
if len(a)>=8:
    strength+=1

lst=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\']
    
if a[0:] in lst:
    strength+=1
print(strength)
