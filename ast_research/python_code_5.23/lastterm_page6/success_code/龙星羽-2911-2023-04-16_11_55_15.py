a=input()
t=''
for i in a:
    t=str((int(i)+5)%10)+t
print(t)
