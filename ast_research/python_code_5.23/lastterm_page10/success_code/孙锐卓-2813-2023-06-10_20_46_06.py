a=input()
b=input()
c=''
for i in a:
    if i not in b:
        c+=i
print(c)
