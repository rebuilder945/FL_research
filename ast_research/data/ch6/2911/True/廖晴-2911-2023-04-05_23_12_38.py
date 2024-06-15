a=input()
s=''
for i in a:
    i=str((int(i)+5)%10)
    s=i+s
print(s)
