a=input()
strength=0
lst=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\']
if a.isupper():
    strength+=1
elif a.islower():
    strength+=1
elif a.isdigit():
    strength+=1
elif len(a)>=8:
    strength+=1


    
elif any(x in lst for x in a):
    strength+=1
print(strength)
