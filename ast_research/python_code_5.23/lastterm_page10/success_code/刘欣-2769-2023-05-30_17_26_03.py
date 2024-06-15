password = input()  
original = ''  
for char in password:
    if char.isalpha():  
        if char.islower(): 
            original += chr(122 - ord(char) + 97) 
        else:  
            original += chr(90 - ord(char) + 65)  
    else: 
        original += char  
print(password)
print(original)
