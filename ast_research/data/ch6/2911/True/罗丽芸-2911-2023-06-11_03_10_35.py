n=input()
a=''
for i in n:
    a=a+str((int(i)+5)%10)
print(a[::-1])


