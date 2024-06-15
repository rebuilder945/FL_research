 
a=input()
temp=''
for i in a:
    temp=str((int(i)+5)%10)+temp
print(temp)

