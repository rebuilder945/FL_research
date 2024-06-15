a=input()
b=input()
for i in range(len(a)):
    if len(a)!=len(b):
        print("False")
        break
    elif a[i] not in b or b[i] not in a:
        print("False") 
    else:
        print("Ture")        
