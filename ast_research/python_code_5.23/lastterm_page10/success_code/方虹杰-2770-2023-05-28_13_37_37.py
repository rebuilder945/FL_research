a=input()
b=list(a)
for i in b:
    if i not in list('qwertyuioplkjhgfdsazxcvbnmZXCVBNMKLJHGFXDSAQWERTYUIOP'):
        print("False")
    else:
        print("True")
