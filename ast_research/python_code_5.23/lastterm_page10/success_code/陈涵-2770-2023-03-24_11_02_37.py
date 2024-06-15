a=input()or""
b=input()or""
flag=False
if a=="" and b=="":
    flag=True
else:
    for i in range(len(a)):
        if len(a)!=len(b):
            break
        elif a[i] not in b or b[i] not in a:
            flag=False
            break 
        else:
            flag=True
print(flag)

                
