a=input()
strength=0
lst=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\']
if a.isupper():
    strength+=1
if a.islower():
    strength+=1
if a.isdigit():
    strength+=1
if len(a)>=8:
    strength+=1


    
if any(x in lst for x in a):
    strength+=1
print(strength)
