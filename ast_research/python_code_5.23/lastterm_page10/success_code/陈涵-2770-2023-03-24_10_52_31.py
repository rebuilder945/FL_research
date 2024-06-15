a=input()
b=input()
flag=False
for i in range(len(a)):
    if len(a)!=len(b):
        break
    elif a[i] not in b or b[i] not in a:
        flag=False
        break 
    else:
        flag=True
print(flag)                
